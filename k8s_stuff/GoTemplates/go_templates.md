
# Go template engine 

* go-templates: https://pkg.go.dev/text/template generate text output based on data-driven templates
* go white spaces: https://pkg.go.dev/text/template#hdr-Text_and_spaces

* go-template usage:
```bash
# add new line char, evething not inside {{}} is treated as a string
kubectl get no -o go-template='Hello, World!{{"\n"}}'

# in order to write a go-template we need to see what fields are available: 
#at top level we have apiVersion and items 
kubectl get po -oyaml 
kubectl get explain po 

# so we can get them things like apiVersion items
kubectl get po -o go-template='{{.apiVersion}}{{"\n"}}'
kubectl get po -o go-template='{{.items}}'

# range: takes an array, slice, map, or channel and loops through
kubectl get po -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'
```

* go-template file usage:

```bash

kubectl get po -o go-template-file=podnode_allocation.gotemplate
```