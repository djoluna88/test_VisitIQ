# monitoring_strategy.py
# The goal is to create alert rules based on severity and routing by channel

class PipelineMonitoring:
    def __init__(self):
        self.metrics = {
            "operational": ["success_rate", "duration", "resource_utilization"],
            "data_quality": ["freshness", "completeness", "validity"],
            "business": ["records_processed", "output_size", "cost_per_run"]
        }
    
    def create_alert_rules(self, pipeline_config):
        """Creates alert rules based on severity"""
        rules = {
            "critical": [
                {"metric": "success_rate", "threshold": "< 90%", "window": "1h"},
                {"metric": "data_freshness", "threshold": "> SLA", "window": "24h"}
            ],
            "warning": [
                {"metric": "duration", "threshold": "> P95", "window": "7d"},
                {"metric": "cost_per_run", "threshold": "> budget", "window": "month"}
            ]
        }
        
        # Alert routing by channel
        routing = {
            "critical": ["pagerduty", "slack-eng-channel", "email-managers"],
            "warning": ["slack-data-channel", "email-owners"]
        }
        
        return self._deploy_cloudwatch_alarms(rules, routing)