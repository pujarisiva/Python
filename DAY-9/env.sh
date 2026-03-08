deploy_configuration() {
    echo "Deploy server agent on $1"
}

environments=("dev" "staging" "prod")
for env in "${environments[@]}"; do
    deploy_configuration "$env"
done

