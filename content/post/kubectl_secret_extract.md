---
date: "2023-01-04"
tags: ["kubectl", "kubernetes"]
title: "One-liner to extract a Kubernetes secret with kubectl"
---

Several of the pods I deploy on Kubernetes use environment variables for configuration. Our Kubernetes clusters pull the vaults from our secrets repository and store them as Kubernetes secrets. Here's a one-liner I can never remember to check the value of a particular secret:

```bash
kubectl get secrets/SECRET_NAME -o json | jq .data.ENV_VAR | sed 's/"//g' | base64 -d
```

As with many of the entries in this blog this is mainly for me but will perhaps be helpful to someone else as well.
