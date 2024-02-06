function createPushNotificationsJobs(jobs, queue) {
  // check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const queueJob = queue.create('push_notification_code_3', job);
    queueJob.save((err) => {
      if (err) {
        console.log('Notification job creation failed', err);
      }
      console.log(`Notification job created: ${queueJob.id}`);
    });

    // listen on completion
    queueJob.on('complete', () => {
      console.log(`Notification job ${queueJob.id} completed`);
    });

    // listen on failure
    queueJob.on('failed', (err) => {
      console.log(`Notification job ${queueJob.id} failed: ${err}`);
    });

    // listen of progress
    queueJob.on('progress', (progress) => {
      console.log(`Notification job ${queueJob.id} ${progress}% complete`);
    });

  });
}

module.exports = createPushNotificationsJobs
