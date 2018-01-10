
SET @tablename='leo.smsbakAfter201508';
 # [Id] [bigint] IDENTITY(1,1) NOT NULL,
 # [UserId] [bigint] NULL,
 # [ReqNum] [varchar](100) NULL,
 # [PhoneNum] [varchar](20) NULL,
 # [SendMessage] [varchar](1000) NULL,
 # [ExtNum] [varchar](100) NULL,
 # [SendDate] [datetime] NULL,
 # [SendStatus] [int] NULL,
 # [RealStatus] [varchar](100) NULL,
 # [ReSendStatus] [int] NULL,
 # [Status] [bit] NULL,
 # [FeeCount] [int] NULL,
 # [pipeID] [int] NULL,
 # [UnionFlag] [varchar](50) NULL,
 # [ReportSend] [int] NULL,


# load data
load data local infile '/root/house/smsbakAfter201508.csv'
into table smsbakAfter201508
fields terminated by ','  optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';



# ETL 清洗导入错误的数据
DELETE 
#SELECT * smsbakAfter201508
FROM leo.smsbakAfter201508
WHERE feecount>10;

# 总计
SELECT COUNT(FeeCount) 
FROM leo.smsbakAfter201508;

##########################

# 按普通短信和长短信条数统计
# countByFeeCount
SELECT FeeCount, COUNT(FeeCount) cont 
FROM leo.smsbakAfter201508
WHERE feeCount<10
GROUP BY FeeCount
ORDER BY cont DESC;


# 统计每个用户的发送量
# sumByUser
SELECT UserId, sum(FeeCount) cont 
FROM leo.smsbakAfter201508
GROUP BY UserId
ORDER BY cont DESC;

# 统计每条通道的发送量
# sumByPip
SELECT pipeID, sum(FeeCount) cont 
FROM leo.smsbakAfter201508
GROUP BY UserId
ORDER BY cont DESC;


#############每天

# 统计每天的发送量
# sumByDay
SELECT Date(SendDate) everyDay, SUM(FeeCount) cont 
FROM leo.smsbakAfter201508
GROUP BY everyDay
ORDER BY everyDay;

# 每天每用户的发送量统计
# sumByUserDaily
SELECT Date(SendDate) everyDay, UserId, SUM(FeeCount) cont
FROM leo.smsbakAfter201508
GROUP by UserId, everyDay
ORDER BY everyDay;

# 每天每种发送状态的统计
# sumByStatusDaily
SELECT Date(SendDate) everyDay, SendStatus, SUM(FeeCount) cont
FROM leo.smsbakAfter201508
GROUP by SendStatus, everyDay
ORDER BY everyDay;

# 每天每条通道的发送量统计
# sumByPipDaily
SELECT Date(SendDate) everyDay, pipeID, SUM(FeeCount) cont
FROM leo.smsbakAfter201508
GROUP by pipeID, everyDay
ORDER BY everyDay;





