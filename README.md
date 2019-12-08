# Introduction
Deep convolutional neural networks have led to a series of breakthroughs in image recognition, which has attracted much attention in recent years. However, since the training and evaluation with deep neural networks are always resource-consuming and time-critical on the local machines, a clustered server for image recognition has been in high demand. In this project, we designed a client-server web application to resolve this problem. Specifically, the client submits any picture which needs to be classified as a website and the server runs the deep learning algorithm to predict the class label and return it back to the client. In such a way, we largely reduce the hardware requirement for the client to run deep CNNs and enhances resource usage at the server end.

# Environment Setup
Following the [instruction](https://piazza.com/class_profile/get_resource/jzoasm3tudz780/k1labuill69703) to reserve a web server on GENI.

To set up the environment on the web server, please install `conda` and use `environment.yml` to install required packages.

Our Rspec is attached as follows:
```angular2
<rspec xmlns="http://www.geni.net/resources/rspec/3" xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" xmlns:tour="http://www.protogeni.net/resources/rspec/ext/apt-tour/1" xmlns:jacks="http://www.protogeni.net/resources/rspec/ext/jacks/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.geni.net/resources/rspec/3    http://www.geni.net/resources/rspec/3/request.xsd" type="request">
  <node xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1" client_id="node-0" component_id="urn:publicid:IDN+instageni.northwestern.edu+node+pc2" component_manager_id="urn:publicid:IDN+instageni.northwestern.edu+authority+cm" exclusive="false" sliver_id="urn:publicid:IDN+instageni.northwestern.edu+sliver+21525">
    <icon xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1" url="https://portal.geni.net/images/Xen-VM.svg"/>
    <routable_control_ip xmlns="http://www.protogeni.net/resources/rspec/ext/emulab/1"/>
    <sliver_type name="emulab-xen">
      <disk_image name="urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU14-64-STD"/>
    </sliver_type>
    <services>
      <login authentication="ssh-keys" hostname="pcvm2-42.instageni.northwestern.edu" port="22" username="pinghu"/>
      <login authentication="ssh-keys" hostname="pcvm2-42.instageni.northwestern.edu" port="22" username="xjhan"/>
      <login authentication="ssh-keys" hostname="pcvm2-42.instageni.northwestern.edu" port="22" username="psohal"/>
      <login authentication="ssh-keys" hostname="pcvm2-42.instageni.northwestern.edu" port="22" username="sunxm"/>
      <login authentication="ssh-keys" hostname="pcvm2-42.instageni.northwestern.edu" port="22" username="matta"/>
      <emulab:console server="vhost2.shared-nodes.emulab-ops.instageni.northwestern.edu"/>
    </services>
    <emulab:vnode hardware_type="pcvm" name="pcvm2-42"/>
    <host ipv4="165.124.51.195" name="node-0.mini-lab-image-res.ch-geni-net.instageni.northwestern.edu"/>
  </node>
  <rs:site_info xmlns:rs="http://www.protogeni.net/resources/rspec/ext/site-info/1">
    <rs:location country="" latitude="41.50588" longitude="-81.609169"/>
  </rs:site_info>
</rspec>
```

# Executing the server
1. git clone our repo.
2. under the repo, please run `server.py` to execute. The server is running at port `13456`

# Classify the image
Please visit `<server_url>:13456` (or using [our public server](http://pcvm2-42.instageni.northwestern.edu:13456/)) and test.