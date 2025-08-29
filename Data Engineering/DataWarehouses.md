Data lake: raw|messy data , petabytes , any kind , difficult to analyze => DL : used by data scientists for big data real time analystics . data catalog is the data source for a data lake that compensate for the lack of structure .
It keeps track of the data source, where is it used? who is the owner? how often the data is uodated ? 
It's good practice in terms of data governance (managing the availability, usability, integrity and security of the data), and guarantees the reproducibility of the processes in case anything unexpected happens. Or if someone wants to reproduce an analysis from the very beginning, starting with the ingestion of the data. Because of the very flexible way data lakes store data, a data catalog is necessary to prevent the data lake becoming a data swamp. It's good practice to have a data catalog referencing any data that moves through your organization, so that we don't have to rely on tribal knowledge, which makes us autonomous, and makes working with the data more scalable. 
Why Data Lakes Are More Cost-Efficient
Data lakes are more cost-efficient because they use cheap object storage, schema-on-read, separation of storage & compute, open formats, and cold storage options. You don’t pay for compute or optimization until you actually need to process the data.

Data warehouse: specific data for specific use , small on the scale of big data , optimized for analytics : used by data scientist for ad-hoc (BI Process) and read only queries.

Data processing: converting raw data to meanfull information.

