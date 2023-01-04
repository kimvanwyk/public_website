---
date: "2023-01-04"
tags: ["python","fastapi","rest","stored proc"]
title: "Dynamically serving REST endpoints for MSSQL stored procedures with FastAPI"
draft: true
---

I needed to serve a large set of Microsoft SQL Server stored procedures as REST endpoints, which I opted to do with [FastAPI](https://fastapi.tiangolo.com/) and the underlying [Pydantic](https://pydantic-docs.helpmanual.io/) library. To avoid having to update the code when the stored procs changed, I wanted the endpoints to be dynamically generated. This was doable but not as smoothly as I'd hoped:

# Listing the stored proc parameters

Getting a dynamic list of the current stored procs and their input and output parameters can be done with a sql query:

```sql
USE database;
SELECT o.name AS [proc_name], par.name AS [param_name], 
types.name AS [param_dtype], par.is_output AS [is_output]
FROM sys.objects o
JOIN sys.schemas s ON o.schema_id = s.schema_id
INNER JOIN sys.procedures p ON o.object_id = p.object_id
INNER JOIN sys.parameters par ON par.object_id = p.object_id
INNER JOIN sys.types ON par.system_type_id = types.system_type_id 
AND par.user_type_id = types.user_type_id
WHERE o.type_desc = 'SQL_STORED_PROCEDURE'
AND s.name = schema
ORDER BY s.name, o.name, par.name
```

This query will yield a set of rows similar to this:

| proc_name | param_name | param_dtype | is_output |
|-----------|------------|-------------|-----------|
| Proc1     | @Param1    | int         | 0         |
| Proc1     | @Param2    | varchar     | 0         |
| Proc1     | @Param3    | varchar     | 1         |
| Proc2     | @Param1    | datetime    | 0         |
| Proc2     | @Param2    | decimal     | 1         |

# Hitting a brick wall with dynamic Pydantic models and FastAPI endpoints

Pydantic supplies the *[create_model](https://docs.pydantic.dev/usage/models/#dynamic-model-creation)* method which could be used pretty easily to create an input and output model for each of the stored procs, looping over all the parameters in the table above.

Unfortunately I couldn't find a way to use dynamic Pydantic models as the basis for FastAPI endpoint declarations. All the conventional FastAPI examples and documentation I could find required static Pydantic models to exist so they could be referred to by name. I did find a few Github issues on the [FastAPI project issue tracker](https://github.com/tiangolo/fastapi/issues) which discussed dynamic endpoints, for example [this one](https://github.com/tiangolo/fastapi/issues). They had clever solutions which unfortunately involved more Pythonic naval gazing and clever tricks than I was comfortable putting into my code, both for my colleagues' benefit and for the benefit of future-me.

I would love to be able to do this with built-in FastAPI behaviour - if I've missed something in the FastAPI docs please get in touch and let me know.
