See the tracing blog below - it still needs to be converted to markdown, including the tables.

https://docs.google.com/document/d/1C1CqhYnaHT7wbhD6hZ8D0eYoq6QSSbFLoruEaf-5JOw/edit?usp=sharing



|Module Name|Usage count (OpenAPS)|Usage count (default)|
|-----------|---------------------|---------------------|
|cmac       |Not loaded           |1                    |
|ecdh_generic|1 (bluetooth)        |2 (bluetooth)        |
|ecc        |1 (ecdh_generic)     |1 (ecdh_generic)     |
|spidev     |2                    |Not loaded           |
|i2c_bcm2835|1                    |Not loaded           |
|spi_bcm2835|0                    |Not loaded           |
|i2c_dev    |2                    |Not loaded           |
|ipv6       |26                   |24                   |



|Subsystem  |# of calls|
|-----------|----------|
|kmem_*     |200990    |
|mm_*       |182471    |
|sched_*    |195241    |
|rcu_*      |223011    |
|irq_*      |1781503   |
|kmalloc    |79801     |
|cpu_idle   |62623     |
|rss_stat   |22130     |
|ipi_*      |42514     |
|sys_*      |148034    |
|vm_*       |60489     |
|task_*     |72813     |
|timer_     |58572     |
|hrtimer_*  |152271    |
|softirq_*  |28860     |
|workqueue_*|6129      |
|writeback_*|3933      |
|ext4_*     |34461     |
|jbd2_*     |2062      |
|block_*    |3590      |
|dwc_otg*   |27701     |
