const _apiHost = window.location.hostname;

async function request(url, params, method = 'GET') {

    const options = {
        method,
        headers: {
          'Content-Type': 'application/json'
        }
    };
    
    
  
}


const get = (url, params) => {
  return request(url, params);
}

const create = (url, params) => {
  return request(url, params, "POST");
}

const update = (url, params) => {
  return request(url, params, "PUT");
}

const remove = (url, params) => {
  return request(url, params, "DELETE");
}
