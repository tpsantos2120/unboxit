async function request(url, data, header = null, method = "GET") {
  const options = {
    method,
  };

  if (data) {
    if (method === "GET" || method === "DELETE") {
      url += data.split(" ").join("+");
    } else {
      options.body = JSON.stringify(data);
      options.headers =
        header == null
          ? { "Content-Type": "application/json" }
          : {
              "Content-Type": "application/json",
              "Authorization": header,
            };
    }
  }

  console.log(url, options, data);
  const response = await fetch(url, options);
  if (response.status !== 200) {
    return response.json();
  }

  const result = await response.json();

  return result;
}

const get = (url, data) => {
  return request(url, data);
};

const create = (url, data, header) => {
  return request(url, data, header, "POST");
};

const update = (url, data, header) => {
  return request(url, data, header, "PUT");
};

const remove = (url, data, header) => {
  return request(url, data, header, "DELETE");
};

export default {
  get,
  create,
  update,
  remove,
};
