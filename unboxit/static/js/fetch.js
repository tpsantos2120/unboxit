const _apiHost = window.location.hostname;

async function request(url, params, method = 'GET') {

    
  
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
