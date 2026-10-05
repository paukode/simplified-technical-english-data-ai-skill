# Technical names: Amazon Web Services (AWS)

These are technical names for AWS services, features, and concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official AWS name is a technical name (rule W5).
For a former product name, refer to Part 5 of `substitutions.md`.

## Global infrastructure and accounts

- Amazon Web Services (AWS), Amazon, AWS Region, Region, Availability Zone, AWS Local Zones, Local Zone, AWS Wavelength, AWS Outposts, edge location, Regional edge cache, AWS GovCloud (US), AWS European Sovereign Cloud
- AWS account, management account, member account, root user, account ID, AWS Organizations, organizational unit (OU), service control policy (SCP), resource control policy (RCP), AWS Control Tower, landing zone, delegated administrator
- AWS Management Console, AWS CLI, AWS SDK, AWS CloudShell, AWS Console Mobile Application, AWS Support, AWS Trusted Advisor, AWS Health Dashboard, AWS Marketplace, AWS Well-Architected Framework, AWS Well-Architected Tool, AWS Free Tier
- Amazon Resource Name (ARN), resource tag, tag key, tag value, service quota, Service Quotas, AWS Resource Groups, Tag Editor, AWS Resource Explorer

## Compute

- Amazon Elastic Compute Cloud (Amazon EC2), EC2 instance, instance type, Amazon Machine Image (AMI), launch template, user data, instance metadata, Instance Metadata Service (IMDS), IMDSv2, Amazon EC2 Auto Scaling, EC2 Auto Scaling, Auto Scaling group
- On-Demand Instance, Spot Instance, Reserved Instance, Dedicated Host, Dedicated Instance, On-Demand Capacity Reservation, Capacity Reservation, placement group, AWS Nitro System, AWS Graviton, Graviton processor, AWS Inferentia, AWS Trainium, EC2 Image Builder
- AWS Lambda, Lambda, Lambda function, Lambda layer, Lambda alias, function URL, execution role, execution environment, event source mapping, provisioned concurrency, reserved concurrency, Lambda SnapStart, Lambda@Edge, CloudFront Functions
- AWS Batch, AWS Elastic Beanstalk, Amazon Lightsail, AWS App Runner, AWS ParallelCluster, AWS Serverless Application Model (AWS SAM)

## Containers

- Amazon Elastic Container Service (Amazon ECS), ECS cluster, task definition, ECS task, ECS service, capacity provider, Amazon ECS Anywhere
- Amazon Elastic Kubernetes Service (Amazon EKS), EKS cluster, managed node group, self-managed node, EKS Auto Mode, EKS Pod Identity, IAM roles for service accounts (IRSA), EKS add-on, Amazon EKS Anywhere
- AWS Fargate, Fargate, Fargate profile, Amazon Elastic Container Registry (Amazon ECR), ECR repository, Amazon ECR Public, AWS Cloud Map, Bottlerocket

## Application integration

- Amazon Simple Queue Service (Amazon SQS), standard queue, FIFO queue, visibility timeout, message retention period, Amazon Simple Notification Service (Amazon SNS), SNS topic, message filtering
- Amazon EventBridge, EventBridge, EventBridge rule, Amazon EventBridge Scheduler, EventBridge Scheduler, Amazon EventBridge Pipes, EventBridge Pipes, event pattern, schema registry
- Amazon MQ, AWS Step Functions, Step Functions, state machine, Standard Workflows, Express Workflows, Amazon API Gateway, API Gateway, HTTP API, WebSocket API, API stage, usage plan, Lambda authorizer, AWS AppSync
- Amazon Simple Email Service (Amazon SES), AWS End User Messaging, Amazon AppFlow

## Storage

- Amazon Simple Storage Service (Amazon S3), S3, S3 bucket, bucket, object, object key, key prefix, prefix, bucket policy, access control list (ACL), S3 Block Public Access, Block Public Access, S3 Object Ownership, S3 Versioning, versioning, S3 Object Lock, Object Lock, legal hold, retention mode, governance mode, compliance mode
- S3 Lifecycle, lifecycle rule, lifecycle configuration, storage class, S3 Standard, S3 Standard-Infrequent Access (S3 Standard-IA), S3 One Zone-Infrequent Access (S3 One Zone-IA), S3 Intelligent-Tiering, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, S3 Express One Zone
- directory bucket, general purpose bucket, Amazon S3 Tables, S3 Tables, table bucket, Amazon S3 Vectors, S3 Vectors, vector bucket, S3 Replication, Cross-Region Replication (CRR), Same-Region Replication (SRR), S3 Batch Operations, S3 Inventory, S3 Storage Lens, S3 Access Points, Multi-Region Access Points, S3 Object Lambda, S3 Transfer Acceleration
- multipart upload, presigned URL, S3 event notification, Mountpoint for Amazon S3, SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, Requester Pays
- Amazon Elastic Block Store (Amazon EBS), EBS volume, EBS snapshot, gp3, gp2, io2, io2 Block Express, st1, sc1, Provisioned IOPS, IOPS, Amazon Data Lifecycle Manager
- Amazon Elastic File System (Amazon EFS), Amazon FSx, Amazon FSx for Lustre, Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, Amazon FSx for OpenZFS, AWS Storage Gateway
- AWS Backup, backup plan, backup vault, recovery point, AWS Backup Vault Lock, AWS Elastic Disaster Recovery, AWS DataSync, AWS Transfer Family, AWS Snowball, AWS Snowball Edge, AWS Snow Family

## Databases

- Amazon Relational Database Service (Amazon RDS), DB instance, DB cluster, DB parameter group, DB subnet group, option group, read replica, Multi-AZ deployment, Multi-AZ DB cluster, Amazon RDS Proxy, RDS Proxy, Amazon RDS Custom
- Amazon RDS for PostgreSQL, Amazon RDS for MySQL, Amazon RDS for MariaDB, Amazon RDS for Oracle, Amazon RDS for SQL Server, Amazon RDS for Db2, Performance Insights, Database Insights, Enhanced Monitoring, automated backup
- Amazon Aurora, Aurora, Aurora PostgreSQL-Compatible Edition, Aurora MySQL-Compatible Edition, Aurora Serverless v2, Aurora Global Database, Amazon Aurora DSQL, Aurora DSQL, Aurora Replica, Aurora I/O-Optimized, Aurora Limitless Database
- Amazon DynamoDB, DynamoDB, DynamoDB table, partition key, sort key, attribute, global secondary index (GSI), local secondary index (LSI), DynamoDB Streams, DynamoDB Accelerator (DAX), global table, on-demand capacity mode, provisioned capacity mode, read capacity unit (RCU), write capacity unit (WCU)
- Amazon ElastiCache, ElastiCache, ElastiCache for Valkey, ElastiCache for Redis OSS, ElastiCache for Memcached, Amazon MemoryDB, Amazon DocumentDB, Amazon Neptune, Amazon Neptune Analytics, Amazon Keyspaces, Amazon Timestream, Amazon Timestream for InfluxDB
- AWS Database Migration Service (AWS DMS), replication instance, DMS task, DMS Schema Conversion, AWS Schema Conversion Tool (AWS SCT)

## Analytics and data

- Amazon Redshift, Amazon Athena, Athena, Athena workgroup, Amazon Athena for Apache Spark, federated query
- AWS Glue, Glue, AWS Glue Data Catalog, Glue Data Catalog, Glue crawler, crawler, Glue job, Glue ETL job, AWS Glue Studio, AWS Glue DataBrew, AWS Glue Data Quality, Glue connection, Glue workflow, Glue trigger, Glue table, Glue database, AWS Glue Schema Registry, data processing unit (DPU)
- Amazon EMR, EMR, Amazon EMR Serverless, EMR Serverless, Amazon EMR on EKS, EMR cluster, EMR Studio, primary node, core node, task node
- Amazon Kinesis, Amazon Kinesis Data Streams, Kinesis Data Streams, Kinesis, Kinesis data stream, Amazon Data Firehose, Firehose stream, Amazon Managed Service for Apache Flink, Amazon Kinesis Video Streams
- Amazon Managed Streaming for Apache Kafka (Amazon MSK), MSK Serverless, MSK Connect, Amazon OpenSearch Service
- AWS Lake Formation, Lake Formation, Lake Formation permissions, LF-Tags, Amazon DataZone, Amazon SageMaker Unified Studio, Amazon SageMaker Lakehouse, Amazon SageMaker Catalog
- Amazon QuickSight, QuickSight, Amazon Quick Suite, QuickSight dashboard, SPICE, Amazon Q in QuickSight, AWS Clean Rooms, AWS Entity Resolution, AWS Data Exchange
- Amazon Managed Workflows for Apache Airflow (Amazon MWAA), zero-ETL integration

## Machine learning and AI

- Amazon SageMaker, SageMaker, Amazon SageMaker AI, SageMaker AI, SageMaker Studio, SageMaker notebook instance, SageMaker training job, SageMaker Pipelines, SageMaker Feature Store, SageMaker Model Registry, SageMaker Model Monitor, SageMaker Clarify, SageMaker Debugger, SageMaker Experiments
- SageMaker JumpStart, SageMaker Ground Truth, SageMaker HyperPod, SageMaker Canvas, SageMaker Autopilot, SageMaker endpoint, real-time endpoint, serverless endpoint, asynchronous inference, batch transform, multi-model endpoint, inference component, SageMaker Processing job, SageMaker Data Wrangler
- Amazon Comprehend, Amazon Comprehend Medical, Amazon Rekognition, Amazon Textract, Amazon Transcribe, Amazon Polly, Amazon Translate, Amazon Lex, Amazon Kendra, Amazon Personalize, Amazon Augmented AI (Amazon A2I), AWS HealthLake

## Generative AI and agents

- Amazon Bedrock, Bedrock, Bedrock model, model access, Amazon Bedrock Knowledge Bases, Bedrock knowledge base, Amazon Bedrock Guardrails, Bedrock guardrail, contextual grounding check, Amazon Bedrock Agents, Bedrock agent, action group, agent alias
- Amazon Bedrock AgentCore, AgentCore, AgentCore Runtime, AgentCore Gateway, AgentCore Memory, AgentCore Identity, AgentCore Observability, AgentCore Code Interpreter, AgentCore Browser
- Amazon Bedrock Flows, Amazon Bedrock Prompt Management, Amazon Bedrock Evaluations, model evaluation job, Amazon Bedrock Marketplace, Amazon Bedrock Data Automation, Provisioned Throughput, cross-Region inference, inference profile, application inference profile
- Converse API, ConverseStream, InvokeModel, InvokeModelWithResponseStream
- Amazon Nova, Amazon Nova Micro, Amazon Nova Lite, Amazon Nova Pro, Amazon Nova Premier, Amazon Nova Canvas, Amazon Nova Reel, Amazon Nova Sonic, Amazon Nova Act, Amazon Titan, Amazon Titan Text Embeddings
- Amazon Q, Amazon Q Business, Amazon Q Developer, Amazon Q Developer in chat applications, Kiro, AWS Transform, Strands Agents, Strands Agents SDK

## Networking and content delivery

- Amazon Virtual Private Cloud (Amazon VPC), VPC, default VPC, public subnet, private subnet, internet gateway, egress-only internet gateway, NAT instance, security group, network access control list (network ACL), elastic network interface (ENI), Elastic IP address
- VPC endpoint, gateway endpoint, interface endpoint, AWS PrivateLink, PrivateLink, endpoint service, VPC peering connection, VPC peering, AWS Transit Gateway, Transit Gateway, transit gateway attachment, AWS Cloud WAN
- AWS Direct Connect, Direct Connect, Direct Connect gateway, AWS Site-to-Site VPN, AWS Client VPN, virtual private gateway, customer gateway, VPC Flow Logs, flow log, Reachability Analyzer, Network Access Analyzer, Amazon VPC IP Address Manager (IPAM), Amazon VPC Lattice
- Elastic Load Balancing (ELB), Application Load Balancer (ALB), Network Load Balancer (NLB), Gateway Load Balancer (GWLB), Classic Load Balancer, target group, listener, listener rule
- Amazon Route 53, Route 53, public hosted zone, private hosted zone, routing policy, alias record, Route 53 Resolver, Route 53 health check
- Amazon CloudFront, CloudFront, CloudFront distribution, origin, origin access control (OAC), cache behavior, cache policy, invalidation, AWS Global Accelerator, AWS Network Firewall, AWS Verified Access

## Security, identity, and compliance

- AWS Identity and Access Management (IAM), IAM, IAM user, IAM group, IAM role, IAM policy, identity-based policy, resource-based policy, managed policy, AWS managed policy, customer managed policy, inline policy, permissions boundary, session policy, policy document, policy statement, principal
- IAM Access Analyzer, access key ID, secret access key, AWS Security Token Service (AWS STS), temporary security credentials, role session, AssumeRole, AWS IAM Identity Center, IAM Identity Center, permission set
- AWS Key Management Service (AWS KMS), KMS key, AWS managed key, customer managed key, key policy, data key, AWS CloudHSM, AWS Secrets Manager, Secrets Manager, AWS Systems Manager Parameter Store, Parameter Store, SecureString parameter
- AWS Certificate Manager (ACM), AWS Private Certificate Authority, AWS WAF, web ACL, AWS Shield, AWS Shield Advanced, AWS Firewall Manager
- Amazon GuardDuty, GuardDuty, GuardDuty finding, Amazon Inspector, Amazon Macie, AWS Security Hub, Security Hub, finding, Amazon Detective, Amazon Security Lake, AWS Artifact, AWS Audit Manager
- Amazon Cognito, Cognito user pool, Cognito identity pool, Amazon Verified Permissions, Cedar, AWS Directory Service, AWS Managed Microsoft AD, AWS Resource Access Manager (AWS RAM), AWS Signer, Signature Version 4 (SigV4)

## Management and governance

- AWS CloudFormation, CloudFormation, CloudFormation stack, CloudFormation template, stack, StackSet, change set, drift detection, AWS Cloud Development Kit (AWS CDK), CDK construct, CDK app, AWS Infrastructure Composer
- AWS Config, AWS Config rule, conformance pack, AWS CloudTrail, CloudTrail, CloudTrail trail, CloudTrail Lake, management event, data event
- AWS Systems Manager, Systems Manager, Session Manager, Run Command, Patch Manager, State Manager, Automation runbook, SSM Agent, AWS Systems Manager Incident Manager
- AWS Service Catalog, AWS License Manager, AWS Compute Optimizer, AWS Resilience Hub, AWS Fault Injection Service (AWS FIS), AWS Launch Wizard, AWS AppConfig

## Monitoring and operations

- Amazon CloudWatch, CloudWatch, CloudWatch metric, CloudWatch alarm, composite alarm, CloudWatch dashboard, Amazon CloudWatch Logs, CloudWatch Logs, CloudWatch Logs Insights, metric filter, subscription filter
- CloudWatch Synthetics, canary, CloudWatch RUM, Container Insights, Lambda Insights, Application Signals, CloudWatch agent, embedded metric format (EMF), AWS X-Ray, X-Ray trace
- Amazon Managed Service for Prometheus, Amazon Managed Grafana, AWS Distro for OpenTelemetry (ADOT), AWS Health, AWS User Notifications, Amazon DevOps Guru

## Cost management

- AWS Billing and Cost Management, AWS Cost Explorer, Cost Explorer, AWS Budgets, AWS Cost and Usage Report (CUR), AWS Data Exports, AWS Cost Anomaly Detection, AWS Pricing Calculator
- Savings Plans, Compute Savings Plans, EC2 Instance Savings Plans, cost allocation tag, AWS Billing Conductor, consolidated billing, billing, data transfer cost, data transfer out

## Developer tools

- AWS CodeBuild, AWS CodeDeploy, AWS CodePipeline, AWS CodeArtifact, AWS CodeCommit, AWS CodeConnections, Amazon CodeGuru, Amazon CodeCatalyst, AWS Amplify, AWS Toolkit

## Migration, end-user computing, and IoT

- AWS Application Migration Service (AWS MGN), AWS Migration Hub, AWS Application Discovery Service, AWS Mainframe Modernization
- Amazon WorkSpaces, Amazon AppStream 2.0, Amazon Connect, Amazon Chime SDK, AWS IoT Core, AWS IoT Greengrass, AWS IoT SiteWise, Amazon Location Service, Amazon Braket, AWS Device Farm
