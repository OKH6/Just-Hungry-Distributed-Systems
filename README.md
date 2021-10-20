# Just Hungry Distributed Systems
A python program that simulates a food ordering service using a fault tolerant distributed system based on passive replication
 
### System Design

![alt text](https://github.com/OKH6/Just-Hungry-Distributed-Systems/blob/main/Diagram.png?raw=true)
### Front-end server

Manages clients requests to a primary server. Primary server can be any of BackEnd 0,1 and 2 based on availability

### Back-end server 


### Client Implementation

allows a user to access the required distributed system by making food ordering requests and receiving system responses.

### Use of web services

Incorporates external web services to support delivery address retrieval by postal code. The implementation treats web services as distributed system component.