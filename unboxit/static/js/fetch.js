async function request(url, data, method = "GET") {
  console.log(data);

  const options = {
    method,
    headers: {
      "Content-Type": "application/json",
    },
  };

  if (data) {
    if (method === 'GET') {
      url += '/' + data.split(' ').join('+');;
    } else {
      options.body = JSON.stringify(params);
    }
  }

  console.log(url, options);
  const response = await fetch(url, options);
  if (response.status !== 200) {
    return response;
  }

  const result = await response.json();

  return result;
}

const get = (url, data) => {
  return request(url, data);
};

const create = (url, data) => {
  return request(url, data, "POST");
};

const update = (url, data) => {
  return request(url, data, "PUT");
};

const remove = (url, data) => {
  return request(url, data, "DELETE");
};

export default {
  get,
  create,
  update,
  remove,
};
