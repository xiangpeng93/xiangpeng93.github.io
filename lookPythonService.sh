basepath=$(cd `dirname $0`; pwd)
cd $basepath

ps -ef | grep main.py |grep -v grep
if [ $? -ne 0 ]
then
echo "restart python service"
nohup python -u /usr/share/nginx/xiangpeng93.github.io/main.py > system.log 2>&1 &
else
echo "service running..."
fi
