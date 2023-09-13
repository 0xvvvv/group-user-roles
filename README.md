# group-user-roles
The script is about grouping roles to each user. Input file is made by GCP project IAM import

1. Get GCP project IAM export with list of users and its roles:
     gcloud projects get-iam-policy PROJECT-ID \
      --flatten="bindings[].members[]" \
      --format="csv(bindings.members,bindings.role)" > PROJECT-ID-USER-ROLES.csv
2. Transform output file into <user, role> format (you have to delete unuseful data)
3. Run script
4. As result you will get list of users and its roles separated by comma 
