# Test_VisitIQ

- In this repository you will be able to find the proposal solution for technical VisitIQ's test
- As per requirement you can see the architecture proposal below: 
<img width="357" height="843" alt="image" src="https://github.com/user-attachments/assets/28bcee5b-55d0-4aa4-a68c-f6357171e4b9" />


  ### Bonus Points (Optional)

| **Strategy** | **Implementation** | **Estimated Savings** |
|--------------|-------------------|----------------------|
| 💾 **Output Compression** | Parquet/ORC + Snappy | **50-80%** storage |
| 📦 **S3 Lifecycle Policies** | Intelligent tiering (Standard → IA → Glacier) | **40-60%** |
| ⚙️ **Pipeline Right-sizing** | Monitoring + automatic worker adjustment | **20-30%** |
| 🔄 **Batch Processing** | Grouping of small executions | **30-40%** |


## Trade OFF Proposal

| Option | Pros | Cons | Decision |
|--------|------|------|----------|
| Airflow vs Step Functions | Greater maturity, community, rich UI | Higher overhead, needs infrastructure | Step Functions for simple pipelines, Airflow for complex DAGs |
| Glue Catalog vs DataHub | AWS-integrated, no extra cost | Limited lineage, less flexible | Glue Catalog + OpenMetadata extended |
| YAML vs JSON configs | More readable, supports comments | Slightly more complex parsing | YAML for humans, JSON Schema for validation |
| Monolith vs Microservices | Simpler to operate, easier debugging | Coupling, scalability issues | Hybrid architecture: central orchestrator + specific executors |
| IAM Roles per pipeline vs shared | Granular security, isolation | Complex management, IAM limits | Per-pipeline roles with permissions boundary |