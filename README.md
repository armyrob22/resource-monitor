This is my own resource monitor app that I'm building to be deployed in a container or to be run in a cluster. I will be adding and testing new features over the next month. These will include-
- Normal container resource usage like cpu, ram, disk, network.

- This will also have logging of errors or alerts that you can set within a range of parameters.

- The error and alert logs will be stored to their own folders.

- There will be a charts available to plot error's or alerts over time to see trends that might be hidden.

- I also want to add the ability for the monitor to be able to monitor clusters like in kubernetes or docker swarm.

- Last there will be deeper metrics to look at that can help troubleshoot performance issues. (more to come on this later)

To run this monitor you can clone the files and build with docker compose version  2.37.1.
- docker compose build

- docker compose up

- This will load the container. you can run it locally or I do have it listening on all addresses to access it remotely.
http://localhost:8051 or http://<server-ip-address>:8051.

- The extra folders are testing logs i created to test the error's and warning functions. you can remove them.