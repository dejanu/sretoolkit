
go-templates: https://pkg.go.dev/text/template generate text output based on data-driven templates


# add new line char, evething not inside {{}} is treated as a string
kubectl get no -o go-template='Hello, World!{{"\n"}}'

# see what fields are available: at top level we have apiVersion and items 
kubectl get no -oyaml 
# so we can get them things like apiVersion items
kubectl get no -o go-template='{{.apiVersion}}{{"\n"}}'
kubectl get no -o go-template='{{.items}}'

# range comes in; it takes an array, slice, map, or channel and loops through
kubectl get no -o go-template='{{range .items}}{{.metadata.name}}{{"\n"}}{{end}}'

