
create_back_up(){
    echo "back upi taken successfully"
}

databases=("db1" "db2" "db3")
for db in "${databases[@]}"; do
     create_back_up "$db"
done     