# Kafka debugging checklist

Work through these in order. Stop at the first step that shows a problem.

## The client cannot reach the broker

1. **Is the broker running?**
   - `docker compose ps` should show `broker` as `Up`, with port 9092 published.
   - `docker compose logs broker` should contain a line saying `Kafka Server started`.
2. **Read the client's own log lines.**
   - Look for lines that start with `%3|` and contain `FAIL`.
   - They name the address the client tried and why it failed. Compare that address with the port `compose.yaml` publishes.
   - A delivery failure with `Message timed out` is only a symptom. The cause is in the `FAIL` lines above it.
3. **Use the address that matches where the client runs.**
   - Python on your machine: `localhost:9092`.
   - Commands run with `docker compose exec broker ...`: `localhost:9092`.
   - `broker:9092` only resolves on Docker's internal network, so it fails from your machine.

## Connected, but no messages

4. **Read the producer output.** `Delivered ... to topic orders, partition P, offset N` means the producer side is fine. Check that the topic name is the one you expect.
5. **Check the topic name.** List the topics and look for near-duplicates, such as `order` next to `orders`:
   `docker compose exec broker /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list`
6. **Check the group's offsets.**
   `docker compose exec broker /opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group order-notifications`
   - `LAG` 0: the group has already read everything.
   - `LAG` above 0 but nothing printing: the consumer is not running, or it never printed an `Assigned partitions` line.
   - `-` in `CURRENT-OFFSET`: the group has never committed an offset.
7. **Check the reset policy.** `auto.offset.reset` only applies when the group has no committed offset. `earliest` starts from the oldest retained event, and `latest` waits for new ones.
