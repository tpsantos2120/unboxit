/**
 * Request builds the url and options which are then passed to fetch,
 * essentially this abstracts the fetch operation to minimise repetitive code.
 *
 * @param {String} url
 * @param {Object} data
 * @param {String} header
 * @param {Object} method
 * @returns
 */
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
              Authorization: header,
            };
    }
  }

  const response = await fetch(url, options);
  if (response.status !== 200) {
    return response.json();
  }

  const result = await response.json();

  return result;
}
/**
 * Return GET response.
 *
 * @param {String} url
 * @param {Object} data
 * @returns
 */
const get = (url, data) => {
  return request(url, data);
};

/**
 * Return POST response.
 *
 * @param {String} url
 * @param {Object} data
 * @param {String} header
 * @returns
 */
const create = (url, data, header) => {
  return request(url, data, header, "POST");
};
/**
 * Return PUT response
 *
 * @param {String} url
 * @param {Object} data
 * @param {String} header
 * @returns
 */
const update = (url, data, header) => {
  return request(url, data, header, "PUT");
};

/**
 *
 * @param {String} url
 * @param {Object} data
 * @param {String} header
 * @returns
 */
const remove = (url, data, header) => {
  return request(url, data, header, "DELETE");
};

export default {
  get,
  create,
  update,
  remove,
};
