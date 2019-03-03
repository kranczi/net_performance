# net_performance
net performance tests and reporting

## Target result
set of nodes participate in frequent and not overlapping set of traffic exchange.  
iperf3 is used for server-client paris. Tests are categorized into:  
1. tcp based; test end after specific volume of data is transferred. Rerdless of the time it takes.  
(note_to_self: kill lagged/queued processes; not allowing them to stack in the low transfer times (due to onnection problems or capacity caps))  
2. udp based; test end after specific time-window ends. Regardless of the volume of data trasnferred.
3. both test results are reported into whisper db; presented in grafana dashboard. One mark/point per reported test results.

## Required setup
Nodes are installed per DC. Nodes are predifined with a specific set of packages. Package requirements are minimal (for the nodes participating in the tests):  
* puppet/ansible
* mtr
* iperf3
* iptables
* python  

For the node aggregating and presenting results:  
* grafana
* graphite
* whisper

## Planned deployment steps
#### Phase 1
Reporting test results
#### Phase 2
Automatic nodes deployment
#### Phase 3
Reporting standard and changed paths
#### Phase 4
Fixing stalled tcp tests
#### Phase 5
Idea: Automatic alerting of not satisfactory results *  
<br>
<br>
<br>
<br>
*when a number of consecutive tests fall below certain treshold an alert is triggered.  
Yet to be checked if test nodes should keep track of results and report based on that.  
Alternative is basing this on grafana alerting feature (challening to tackle consecutive low values vs a single one-off)  
