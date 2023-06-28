
# start jenkins and ignore hangup

 nohup java -jar jenkins.war --httpPort=-1 --httpsPort=9443 --httpsKeyStore="/path/to/certstore.jks" --httpsKeyStorePassword=[PASSWORD] > nohup.out 2>&1 &
 
 # plugins .hpi and script console
 
 println(hudson.util.Secret.decrypt("{HASH=}")) OR println(hudson.util.Secret.fromString("{XXX= HASH}").getPlainText())
 println(hudson.util.Secret.fromString("some_text").getEncryptedValue())

 
