const kue = require('kue');

const queue = kue.createQueue();

// create object containin the job data
const obj = {
  'phoneNumber': '4153518780',
  'message': 'This is the code to verify your account'
};

// create queue named push_notification_code, create a job with obj
const job = queue.create('push_notification_code', obj);
job.save((err) => {
  if (err) {
    console.log('Notification job error', err);
  }
  console.log('Notification job created:', job.id);
});

// when job is completed log to console
job.on('complete', () => {
  console.log('Notification job completed');
});

// listen for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});
