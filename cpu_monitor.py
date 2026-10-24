cpu_usage = 70

if cpu_usage >= 85:
    print("WARNING: High CPU usage")
elif cpu_usage >= 50:
    print("NOTICE: CPU usage is moderate")
else:
    print("CPU usage is normal")

print("InfraPulse monitoring check complete.")
