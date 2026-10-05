# Technical names: Google Cloud

These are technical names for Google Cloud services, features, and concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official Google Cloud name is a technical name (rule W5).
For a former product name, refer to Part 5 of `substitutions.md`.

## Resources, projects, and access

- Google Cloud, Google Cloud Platform (GCP), Google, Google Cloud console, Cloud Shell, Google Cloud CLI, gcloud CLI, gcloud, bq command-line tool, Cloud Client Libraries
- organization, folder, project, project ID, project number, resource hierarchy, label, region, zone, multi-region, dual-region, Google Cloud Marketplace, Service Usage API, Cloud Resource Manager
- Organization Policy Service, organization policy, Assured Workloads, Google Cloud Sovereign Cloud, quota, API quota

## Compute

- Compute Engine, VM instance, machine type, machine family, custom machine type, instance template, managed instance group (MIG), unmanaged instance group, Spot VM, preemptible VM, sole-tenant node, Shielded VM, Confidential VM
- Persistent Disk, Hyperdisk, Local SSD, disk snapshot, startup script, metadata server, Cloud TPU, Cloud GPUs, Google Cloud Batch, Google Cloud VMware Engine, Bare Metal Solution

## Containers

- Google Kubernetes Engine (GKE), GKE Autopilot, GKE Standard, GKE Enterprise, Workload Identity Federation for GKE, GKE Gateway controller, Config Sync, Policy Controller, Cloud Service Mesh, Container-Optimized OS
- Artifact Registry, Cloud Build, Cloud Deploy, Binary Authorization

## Serverless and application integration

- Cloud Run, Cloud Run service, Cloud Run job, Cloud Run functions, revision, App Engine, App Engine standard environment, App Engine flexible environment, Eventarc, Cloud Scheduler, Cloud Tasks, Workflows
- Pub/Sub, Pub/Sub topic, Pub/Sub subscription, push subscription, pull subscription, BigQuery subscription, Cloud Storage subscription, dead-letter topic, delivery attempt, maximum delivery attempts, message ordering, ordering key, exactly-once delivery, acknowledgment deadline
- API Gateway, Apigee, Apigee X, Cloud Endpoints, Application Integration, Integration Connectors

## Storage

- Cloud Storage, Cloud Storage bucket, Standard storage, Nearline storage, Coldline storage, Archive storage, Autoclass, Object Lifecycle Management, Object Versioning, retention policy, Bucket Lock, object hold, uniform bucket-level access, signed URL
- Storage Transfer Service, Transfer Appliance, Filestore, Cloud Storage FUSE, Backup and DR Service, Google Cloud NetApp Volumes

## Databases

- Cloud SQL, Cloud SQL for PostgreSQL, Cloud SQL for MySQL, Cloud SQL for SQL Server, Cloud SQL Auth Proxy, AlloyDB for PostgreSQL, AlloyDB, AlloyDB Omni, AlloyDB AI
- Spanner, Bigtable, Firestore, Firestore in Datastore mode, Firebase, Firebase Realtime Database, Memorystore, Memorystore for Redis, Memorystore for Valkey, Memorystore for Memcached, Database Migration Service, Datastream

## BigQuery and analytics

- BigQuery, BigQuery dataset, dataset, BigQuery table, partitioned table, ingestion-time partitioning, time-unit column partitioning, integer-range partitioning, clustered table, BigQuery slot, slot, reservation, capacity commitment
- BigQuery editions, Standard edition, Enterprise edition, Enterprise Plus edition, on-demand pricing, capacity pricing, BI Engine, BigQuery ML, BigQuery Omni, BigLake, BigLake table, BigQuery Studio, BigQuery Data Transfer Service
- BigQuery Storage Write API, BigQuery Storage Read API, authorized view, authorized dataset, column-level security, policy tag, query job, dry run, scheduled query, BigQuery sharing, Analytics Hub, object table, BigQuery DataFrames, BigQuery vector search
- Dataform, Looker, LookML, Looker Studio, Looker Studio Pro, Connected Sheets

## Data processing and integration

- Dataflow, Dataflow template, Dataflow Prime, Dataproc, Dataproc cluster, Dataproc Serverless, Google Cloud Serverless for Apache Spark, Dataproc Metastore, Cloud Composer, Cloud Data Fusion
- Dataplex, Dataplex Universal Catalog, data quality scan, data profile scan, Google Cloud Managed Service for Apache Kafka

## AI and machine learning

- Vertex AI, Vertex AI Studio, Vertex AI Workbench, Colab Enterprise, Vertex AI Pipelines, Vertex AI Feature Store, Vertex AI Model Registry, Vertex AI endpoint, online prediction, batch prediction, custom training job, Vertex AI Experiments, Vertex ML Metadata, Vertex AI Model Monitoring, Vertex AI Vizier, AutoML, Model Garden
- Vertex AI Vector Search, Vertex AI Search, Vertex AI Agent Builder, Vertex AI Agent Engine, Agent Development Kit (ADK), Agent Garden, Vertex AI RAG Engine, Gen AI evaluation service, grounding with Google Search
- Document AI, Document AI processor, Cloud Vision API, Video Intelligence API, Speech-to-Text, Text-to-Speech, Cloud Translation, Cloud Natural Language API, Dialogflow CX, Dialogflow ES, Conversational Agents, Contact Center AI (CCAI), Customer Engagement Suite

## Gemini and generative AI

- Gemini, Gemini API, Gemini Developer API, Gemini API in Vertex AI, Gemini Pro, Gemini Flash, Gemini Flash-Lite, Gemini Nano, Gemma, Imagen, Veo, Lyria, Chirp
- Gemini Code Assist, Gemini Cloud Assist, Gemini in BigQuery, Gemini for Google Cloud, Gemini Enterprise, Google AI Studio, NotebookLM, context caching, safety settings, thinking budget, Live API, Gemini CLI

## Networking

- Virtual Private Cloud (VPC), VPC network, auto mode VPC network, custom mode VPC network, subnetwork, hierarchical firewall policy, Cloud Next Generation Firewall (Cloud NGFW), Cloud NAT, Cloud Router, Cloud VPN, HA VPN
- Cloud Interconnect, Dedicated Interconnect, Partner Interconnect, Cross-Cloud Interconnect, Cloud Load Balancing, Application Load Balancer, Network Load Balancer, backend service, URL map, forwarding rule, target proxy, network endpoint group (NEG), serverless NEG
- Cloud CDN, Media CDN, Cloud DNS, Cloud Domains, Cloud Armor, Cloud Armor security policy, Private Service Connect, Private Google Access, Serverless VPC Access, Direct VPC egress, Shared VPC, host project, service project, VPC Network Peering
- VPC Service Controls, service perimeter, access level, Network Connectivity Center, Network Intelligence Center, Network Service Tiers, Premium Tier, Standard Tier, Secure Web Proxy

## Security and identity

- Identity and Access Management (IAM), IAM role, basic role, predefined role, custom role, IAM policy, allow policy, deny policy, principal, service account, service account key, service account impersonation, Workload Identity Federation, workload identity pool, Google group
- Cloud Identity, Identity-Aware Proxy (IAP), Identity Platform, Chrome Enterprise Premium, Secret Manager, Cloud Key Management Service (Cloud KMS), key ring, CryptoKey, Cloud HSM, Cloud External Key Manager (Cloud EKM), customer-managed encryption key (CMEK), customer-supplied encryption key (CSEK)
- Certificate Manager, Certificate Authority Service, Security Command Center, Sensitive Data Protection, Cloud Audit Logs, Admin Activity audit log, Data Access audit log, Access Transparency, Access Approval, Policy Intelligence, Policy Analyzer, IAM Recommender
- reCAPTCHA, Google Security Operations, Mandiant, Web Security Scanner, Confidential Computing

## Operations and observability

- Google Cloud Observability, Cloud Logging, log bucket, log sink, Log Router, log-based metric, Logs Explorer, Log Analytics, Cloud Monitoring, alerting policy, Cloud Trace, Cloud Profiler, Error Reporting
- Google Cloud Managed Service for Prometheus, Ops Agent, Cloud Asset Inventory, Active Assist, Recommender, Personalized Service Health, Google Cloud Service Health

## Cost management

- Cloud Billing, Cloud Billing account, billing account, budget alert, billing export, committed use discount (CUD), sustained use discount (SUD), FinOps hub, Google Cloud Pricing Calculator

## Developer tools

- Cloud Code, Cloud Workstations, Cloud Source Repositories, Secure Source Manager, Infrastructure Manager, Config Connector, Firebase Studio, Jules
