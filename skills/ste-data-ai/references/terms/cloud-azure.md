# Technical names: Microsoft Azure

These are technical names for Microsoft Azure services, features, and concepts.
Use them as nouns, or as modifiers before a noun.
Do not use a technical name as a verb (rule W6).
Use the official spelling and case.
A name in parentheses is the short name or the acronym. Write the full name at the first use (rule W7).
This list is not complete. Any official Azure name is a technical name (rule W5).
For a former product name, refer to Part 5 of `substitutions.md`.

## Accounts, subscriptions, and governance

- Microsoft Azure, Azure, Microsoft, Azure portal, Azure CLI, Azure PowerShell, Azure Cloud Shell, Azure Resource Manager (ARM), ARM template, Bicep, Bicep file
- tenant, Azure tenant, management group, subscription, resource group, resource provider, resource ID, resource lock, Azure Policy, policy definition, policy initiative, policy assignment, Azure landing zone, Cloud Adoption Framework, Azure Well-Architected Framework
- Azure Advisor, Azure Resource Graph, paired region, availability set, update domain, Azure Marketplace, Azure Lighthouse, Azure Arc, Azure Local, Azure Government

## Identity and security

- Microsoft Entra ID, Microsoft Entra, Entra ID, Microsoft Entra External ID, app registration, enterprise application, service principal, managed identity, system-assigned managed identity, user-assigned managed identity, workload identity federation
- Conditional Access, Conditional Access policy, Privileged Identity Management (PIM), Microsoft Entra ID Protection, Microsoft Entra Connect, Microsoft 365 group
- Azure role-based access control (Azure RBAC), role definition, built-in role, custom role, Owner role, Contributor role, Reader role
- Azure Key Vault, Key Vault, key vault, Azure Key Vault Managed HSM, Azure Dedicated HSM, soft delete, purge protection
- Microsoft Defender for Cloud, Microsoft Sentinel, Microsoft Defender XDR, Azure DDoS Protection, Azure Firewall, Azure Firewall Manager, Azure Web Application Firewall, Azure Bastion, network security group (NSG), application security group (ASG)
- Azure confidential computing, Microsoft Azure Attestation, Microsoft cloud security benchmark

## Compute

- Azure Virtual Machines, Azure virtual machine, VM size, Azure Virtual Machine Scale Sets, Virtual Machine Scale Sets, Azure Spot Virtual Machines, Azure Dedicated Host, managed disk, OS disk, data disk, temporary disk, Azure Compute Gallery, VM extension
- Azure Batch, Azure Virtual Desktop, Azure VMware Solution, Azure CycleCloud

## Containers

- Azure Kubernetes Service (AKS), AKS cluster, AKS Automatic, system node pool, user node pool, Azure CNI, kubenet, Azure Container Registry (ACR), Azure Container Apps, Container Apps environment, Azure Container Instances (ACI), Azure Red Hat OpenShift, Azure Kubernetes Fleet Manager, Dapr

## Serverless and integration

- Azure Functions, function app, Flex Consumption plan, Consumption plan, Premium plan, Durable Functions, Azure App Service, App Service plan, deployment slot, Azure Static Web Apps
- Azure Logic Apps, logic app, Azure Service Bus, Service Bus queue, Service Bus topic, Azure Event Hubs, event hub, Event Hubs namespace, consumer group, Azure Event Grid, Event Grid topic, Event Grid subscription
- Azure API Management (APIM), API Management, Azure Relay, Azure SignalR Service, Azure Web PubSub, Azure Communication Services, Azure Notification Hubs

## Storage

- Azure Storage, storage account, Azure Blob Storage, blob, blob container, access tier, hot tier, cool tier, cold tier, archive tier, Azure Data Lake Storage Gen2 (ADLS Gen2), Azure Data Lake Storage, hierarchical namespace
- Azure Files, file share, Azure File Sync, Azure Queue Storage, Azure Table Storage, Azure Disk Storage, Azure Managed Disks, Azure Elastic SAN, Azure NetApp Files
- Azure Backup, Recovery Services vault, Backup vault, Azure Site Recovery, shared access signature (SAS), SAS token, stored access policy
- locally redundant storage (LRS), zone-redundant storage (ZRS), geo-redundant storage (GRS), geo-zone-redundant storage (GZRS), read-access geo-redundant storage (RA-GRS), immutable storage, blob versioning, lifecycle management policy
- AzCopy, Azure Storage Explorer, Azure Data Box, Azure Import/Export service

## Databases

- Azure SQL, Azure SQL Database, Azure SQL Managed Instance, SQL Server on Azure Virtual Machines, elastic pool, Hyperscale service tier, General Purpose service tier, Business Critical service tier, vCore purchasing model, DTU purchasing model, serverless compute tier
- Azure Database for PostgreSQL, Azure Database for PostgreSQL flexible server, Azure Database for MySQL, Azure Database for MySQL flexible server, Azure Database Migration Service
- Azure Cosmos DB, Azure Cosmos DB for NoSQL, Azure Cosmos DB for MongoDB, Azure Cosmos DB for Apache Cassandra, Azure Cosmos DB for Apache Gremlin, Azure Cosmos DB for Table, Azure Cosmos DB for PostgreSQL
- request unit (RU), logical partition, physical partition, change feed, consistency level, strong consistency, bounded staleness, session consistency, consistent prefix, eventual consistency
- Azure Cache for Redis, Azure Managed Redis

## Analytics and data

- Microsoft Fabric, Fabric, Fabric capacity, capacity unit (CU), F SKU, Fabric workspace, OneLake, OneLake shortcut, shortcut, Fabric lakehouse, Fabric Data Warehouse, Fabric warehouse, SQL analytics endpoint
- Data Factory in Microsoft Fabric, Dataflow Gen2, Fabric notebook, Spark job definition, Real-Time Intelligence, Eventstream, Eventhouse, KQL database, KQL queryset, Activator, Real-Time hub
- semantic model, Direct Lake, mirroring, Fabric mirroring, Copilot in Fabric, Fabric data agent
- Power BI, Power BI report, Power BI dashboard, Power BI Desktop, Power BI service, Power Query, Data Analysis Expressions (DAX)
- Azure Synapse Analytics, Synapse workspace, dedicated SQL pool, serverless SQL pool, Apache Spark pool, Synapse pipeline, Azure Synapse Link
- Azure Data Factory (ADF), Data Factory, ADF pipeline, activity, Copy activity, mapping data flow, linked service, integration runtime, Azure integration runtime, self-hosted integration runtime, Azure-SSIS integration runtime, schedule trigger, tumbling window trigger, storage event trigger
- Azure Databricks, Azure Stream Analytics, Stream Analytics job, Azure Data Explorer, Kusto, Kusto Query Language (KQL), Azure Analysis Services, Azure HDInsight, Azure Data Share
- Microsoft Purview, Microsoft Purview Data Map, Microsoft Purview Unified Catalog, sensitivity label

## AI and machine learning

- Microsoft Foundry, Foundry project, Foundry Models, Foundry Agent Service, Azure OpenAI, Azure OpenAI in Foundry Models, model deployment, Global Standard deployment, Standard deployment, provisioned deployment, Data Zone deployment, provisioned throughput unit (PTU), tokens per minute (TPM), requests per minute
- Azure AI Search, search index, indexer, skillset, semantic ranker, integrated vectorization, Azure AI Content Safety, Prompt Shields, groundedness detection
- Azure AI services, Azure AI Document Intelligence, Azure AI Speech, Azure AI Language, Azure AI Translator, Azure AI Vision, Azure AI Video Indexer, Azure AI Content Understanding, Azure Bot Service
- Azure Machine Learning, Azure Machine Learning workspace, compute instance, compute cluster, serverless compute, managed online endpoint, batch endpoint, Azure Machine Learning registry, prompt flow, automated machine learning, responsible AI dashboard
- Microsoft Copilot Studio, Copilot Studio, Microsoft 365 Copilot, Microsoft Copilot, Semantic Kernel, Microsoft Agent Framework, Phi

## Networking

- Azure Virtual Network, virtual network (VNet), address space, VNet peering, global VNet peering, Azure Virtual Network Manager, user-defined route (UDR), service endpoint, private endpoint, Azure Private Link, Private Link service
- Azure Private DNS, private DNS zone, Azure DNS, Azure DNS Private Resolver, Azure NAT Gateway, Azure Load Balancer, Azure Application Gateway, Application Gateway for Containers, Azure Front Door, Azure Traffic Manager
- Azure VPN Gateway, VPN gateway, local network gateway, point-to-site VPN, Azure ExpressRoute, ExpressRoute, ExpressRoute circuit, Azure Virtual WAN, virtual hub, Azure Network Watcher, NSG flow logs, VNet flow logs, Connection Monitor, public IP address, service tag

## Monitoring and management

- Azure Monitor, Azure Monitor Logs, Log Analytics workspace, Log Analytics, Azure Monitor Metrics, Application Insights, Azure Monitor alerts, action group, Azure Monitor Agent, data collection rule (DCR), diagnostic setting, activity log, resource log, Azure Workbooks
- Azure Managed Grafana, Azure Monitor managed service for Prometheus, Azure Service Health, Azure Resource Health, Azure Automation, Azure Update Manager, Azure Chaos Studio, Azure Load Testing, Azure Migrate

## Cost management

- Microsoft Cost Management, Cost Management, Azure Reservations, Azure savings plan for compute, Azure Hybrid Benefit, billing profile, invoice section, Enterprise Agreement (EA), Microsoft Customer Agreement (MCA), pay-as-you-go, Azure Pricing Calculator, budget, cost alert

## DevOps and developer tools

- Azure DevOps, Azure Boards, Azure Repos, Azure Artifacts, Azure Test Plans, GitHub Codespaces, GitHub Advanced Security, Azure Developer CLI (azd), Azure App Configuration, Azure Deployment Environments, Microsoft Dev Box

## Hybrid, IoT, and other

- Azure Stack Edge, Azure Stack Hub, Azure IoT Hub, Azure IoT Operations, Azure Digital Twins, Azure Maps, Azure Quantum
