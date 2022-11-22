# That is happening because rabbit MQ is not being installed correctly on Windows (and this error is misleading!). So to solve it do the following:

# type "cmd" in Cortana search or in "Run" for older version of Windows
# right click on in and choose "Run as Administrator"
# go to rabbit's sbin folder (cd "C:\Program Files\RabbitMQ Server\rabbitmq_server-3.7.4\sbin")
# run: rabbitmq-service remove
# run: rabbitmq-service install
# now you can run 6. rabbitmq-plugins enable rabbitmq_management 7. rabbitmq-service start 8. and, finally, run: start http://localhost:15672 9. log on as user "guest" with password: "guest" and that's it. Happy Rabbiting!