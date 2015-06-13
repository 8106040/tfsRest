var rest = require('./restler');

rest.get('http://google.com').on('complete', function(result) {
  if (result instanceof Error) {
    console.log('Error:', result.message);
    this.retry(5000); // try again after 5 sec
  } else {
    console.log(result);
  }
});

rest.get('http://twaud.io/api/v1/users/danwrong.json').on('complete', function(data) {
  console.log(data[0].message); // auto convert to object
});

rest.get('http://twaud.io/api/v1/users/danwrong.xml').on('complete', function(data) {
  console.log(data[0].sounds[0].sound[0].message); // auto convert to object
});

rest.get('http://someslowdomain.com',{timeout: 10000}).on('timeout', function(ms){
  console.log('did not return within '+ms+' ms');
}).on('complete',function(data,response){
  console.log('did not time out');
});

rest.post('http://user:pass@service.com/action', {
  data: { id: 334 },
}).on('complete', function(data, response) {
  if (response.statusCode == 201) {
    // you can get at the raw response like this...
  }
});

// multipart request sending a 321567 byte long file using https
rest.post('https://twaud.io/api/v1/upload.json', {
  multipart: true,
  username: 'danwrong',
  password: 'wouldntyouliketoknow',
  data: {
    'sound[message]': 'hello from restler!',
    'sound[file]': rest.file('doug-e-fresh_the-show.mp3', null, 321567, null, 'audio/mpeg')
  }
}).on('complete', function(data) {
  console.log(data.audio_url);
});

// create a service constructor for very easy API wrappers a la HTTParty...
Twitter = rest.service(function(u, p) {
  this.defaults.username = u;
  this.defaults.password = p;
}, {
  baseURL: 'http://twitter.com'
}, {
  update: function(message) {
    return this.post('/statuses/update.json', { data: { status: message } });
  }
});

var client = new Twitter('danwrong', 'password');
client.update('Tweeting using a Restler service thingy').on('complete', function(data) {
  console.log(data);
});

// post JSON
var jsonData = { id: 334 };
rest.postJson('http://example.com/action', jsonData).on('complete', function(data, response) {
  // handle response
});

// put JSON
var jsonData = { id: 334 };
rest.putJson('http://example.com/action', jsonData).on('complete', function(data, response) {
  // handle response
});
