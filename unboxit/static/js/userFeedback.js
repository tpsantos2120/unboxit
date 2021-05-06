/**
 * Process message to feedback user.
 *
 * @param {String} message
 * @param {String} id
 */
const userFeedback = (message, id) => {
  const userMessage = document.querySelector(id);
  if (userMessage) {
    userMessage.innerText = message;
  }
};
/**
 * Add spinner to modal.
 *
 * @param {String} id
 */
const startSpinner = (id) => {
  const spinner = document.querySelector(id);
  if (spinner) {
    spinner.setAttribute("uk-spinner", "");
  }
};
/**
 * Stop spinner in modal.
 *
 * @param {String} id
 */
const stopSpinner = (id) => {
  const spinner = document.querySelector(id);
  if (spinner) {
    spinner.removeAttribute("uk-spinner", "");
  }
};

/**
 * Display modal with given ID.
 *
 * @param {String} id
 */
const showModal = (id) => {
  const dashboard = document.querySelector(id);
  if (dashboard) {
    UIkit.modal(dashboard, { bgClose: false }).show();
  }
};

/**
 * Hide modal with given ID.
 *
 * @param {String} id
 */
const hideModal = (id) => {
  const dashboard = document.querySelector(id);
  if (dashboard) {
    UIkit.modal(dashboard).hide();
  }
};

export default {
  userFeedback,
  startSpinner,
  stopSpinner,
  showModal,
  hideModal,
};
