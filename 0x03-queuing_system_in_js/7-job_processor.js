const kue = require('kue');
const queue = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // track progress of the job
  job.progress(0, 100);
    
  // check if phoneNumber is blacklisted
  if (blacklist.includes(phoneNumber)) {
    // fail the job
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // track progress to 50%
  job.progress(50, 100);
      
  // log sending notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  //set timeout
  setTimeout(() => {
    done();
  }, 1000);
}

// process jobs from queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
