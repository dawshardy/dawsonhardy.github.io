---
layout: default
title: Why speed tests don’t hit 10/20G
---

A quick reminder for future me:

- Many built-in “speed test” tools are limited by the **remote server**, not your WAN.
- Your endpoint (PC/NIC) may be **1G/2.5G** even if the uplink is higher.
- Single TCP streams often don’t saturate fast links — use multi-stream testing.
- Disk, CPU, and driver offload settings can bottleneck before the network.

Next time: document a repeatable test method (iperf3 local + multi-stream).
