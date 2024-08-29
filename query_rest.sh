curl -X POST https://161.35.XXX.XXX/events/restSearch \
  -k \
  -H "Authorization: XXXXX"\
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
       "returnFormat": "json",
       "type": "url",
       "timestamp": "30d",
       "to_ids": true
       }' |  jq -r '.response[]?.Event.Attribute[] | select(.type == "url") | .value'
