const userFeedback = (message , id) => {
    const userMessage = document.querySelector(id);
    if (userMessage) {
      userMessage.innerText = message;
    }
  };
  const startSpinner = (id) => {
    const spinner = document.querySelector(id);
    if (spinner) {
      spinner.setAttribute("uk-spinner", "");
    }
  };
  const stopSpinner = (id) => {
    const spinner = document.querySelector(id);
    if (spinner) {
      spinner.removeAttribute("uk-spinner", "");
    }
  };
  
  const showModal = (id) => {
    const dashboard = document.querySelector(id);
    if (dashboard) {
      UIkit.modal(dashboard, { bgClose: false }).show();
    }
  };
  
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
    hideModal
  };