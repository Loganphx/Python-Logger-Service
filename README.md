# Phoenix Log


Log Levels

    LOG
    DEBUG
    WARNING
    ERROR
    EXCEPTION
### Logger
    
    # Only needs to created once as it creates an singleton/instance that is accessable from anywhere
    logger = new Logger()
    
## Sink Types
FileSink (.txt) - Outputs logs to a file in format [LogType, LogMessage, TimeStamp]

    # Writes Logs, Debugs, Warnings, Errors and Exceptions to file 
    file_sink = FileSink(LogLevels.LOG, "logging.txt")
    logger.subscribe_sink(file_sink)

FileSink (.csv) - Exact same as the text file sink, except it adds a CSV Header to properly format the file.

    # Writes Warnings, Errors and Exceptions to file, and ignores logs and debugs
    file_sink = FileSink(LogLevels.WARNING, "logging.csv") 
    logger.subscribe_sink(file_sink)
  
 WebHookSink - Utilizes Web Hooks and Requests to post logging to the api source of choice.

    webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    # Posts Errors and Exceptions to Web Hook
    webhook_sink = WebHookSink(LogLevels.ERROR, webhook_url)
    logger.subscribe_sink(webhook_sink)
  
 DiscordWebHookSink - Utilizes Discord Web Hooks to allow for posting to channels of choice.

    discord_webhook_url = "https://ptb.discord.com/webhook/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    # Posts Errors and Exceptions to Discord
    discord_webhook_sink = WebHookSink(LogLevels.ERROR, discord_webhook_url)
    logger.subscribe_sink(discord_webhook_sink)
  	
 SqlSink - Planned Functionality.

    sql_connection_string = "Server=(local);Database=Sample"
    # Writes Debugs, WARNINGS, ERRORS AND EXCEPTIONS TO SQL
    sql_sink = SqlSink(LogLevels.DEBUG, sql_connection_string)
    logger.subscribe_sink(sql_sink)

## Examples
Sink Chaining

    # Writes Logs, Debugs, WARNINGS, ERRORS AND EXCEPTIONS TO logging.txt
    file_sink = FileSink(LogLevels.LOG, "logging.txt")
    # Writes WARNINGS, ERRORS AND EXCEPTIONS TO logging.csv
    csv_file_sink = FileSink(LogLevels.WARNING, "logging.csv")
    discord_webhook_url = "https://ptb.discord.com/webhook/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    # Posts ERRORS AND EXCEPTIONS TO Discord
    discord_webhook_sink = DiscordWebHookSink(LogLevels.ERROR, discord_webhook_url)

    # You can chain sinks two ways, 3 lines
    logger.subscribe_sink(file_sink)
    logger.subscribe_sink(csv_file_sink)
    logger.subscribe_sink(discord_webook_sink)
    # or all in 1 line
    logger.subscribe_sink(file_sink).subscribe_sink(csv_file_sink).subscribe_sink(discord_webook_sink)