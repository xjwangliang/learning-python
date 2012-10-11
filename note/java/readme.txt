wget -c http://download.oracle.com/otn-pub/java/jdk/7/jdk-7-linux-i586.tar.gz 

sudo tar zxvf ./jdk-7-linux-i586.tar.gz  -C /usr/lib/jvm
cd /usr/lib/jvm
sudo mv jdk1.7.0/ java-7-sun


vim ~/.bashrc





export JAVA_HOME=/home/wang/Desktop/C/jdk1.7.0_07
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH


source ~/.bashrc



sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-7-sun/bin/java 300
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-7-sun/bin/javac 300
sudo update-alternatives --install /usr/bin/jar jar /usr/lib/jvm/java-7-sun/bin/jar 300 
sudo update-alternatives --install /usr/bin/javah javah /usr/lib/jvm/java-7-sun/bin/javah 300 
sudo update-alternatives --install /usr/bin/javap javap /usr/lib/jvm/java-7-sun/bin/javap 300 




sudo update-alternatives --config java  



Eclipse 3.6 在 Ubuntu 10.04 下会出现一个很奇怪的现象，我没有经过测试，无法确定是Ubuntu 10.04 还是 JDK 还是 Eclipse本身造成的。 这个现象是：

可以在终端顺利启动Eclipse，但是鼠标双击，或者用起动器启动就会出现如下的内容：

A Java RunTime Environment (JRE) or Java Development Kit (JDK) must be available in order to run Eclipse. No java virtual machine was found after searching the following locations:…

解决办法是在终端进入你的eclipse目录，然后输入：

mkdir jre
cd jre
ln -s 你的JDK目录/bin bin
