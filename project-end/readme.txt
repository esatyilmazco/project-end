note= we installed it via kubernetes cluster in aws.

Step 1: Install Docker
Step 2: Install Kubectl
Step 3: Install Go
Step 4:  Install Kind 
Step 5: Update Go Path
Step 6: Create a K8s Cluster
Step 7: Verify K8s Cluster 
Step 8: Try Your Cluster


1. curl -fsSL https://download.docker.com/linux/ubu... | sudo apt-key add - && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && sudo apt-get install docker-ce -y
2. curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)..." && sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
3. wget https://golang.org/dl/go1.15.8.linux-... && sudo tar -C /usr/local -xzf go1.15.8.linux-amd64.tar.gz && export PATH=$PATH:/usr/local/go/bin
4. GO111MODULE="on" go get sigs.k8s.io/kind@v0.10.0 && sudo su
5. export PATH=$PATH:/home/ubuntu/go/bin
6. kind create cluster
-----------------------------------------------------------------------------------------------------------
Create and add the following files in order.
7.docker-compose.yml create
8.fluent-usage/Dockerfile create Dockerfile
9.fluent/configuration/fluentfile.conf
10.Run it with the command below.
    -docker-compose up --detach
11.We need to already have an EFK configuration.
12.kubectl apply -f deployment.yml
13.kubectl apply -f svc.yml
15.kubectl apply -f svcaccount.yml
16.kubectl apply -f cluster-role.yml
17.kubectl apply -f cluster-role-binding.yml
18.kubectl apply -f configmapfile.yml
19.kubectl apply -f daemonset-file.yml
20.python app on cli screen(application.py)


