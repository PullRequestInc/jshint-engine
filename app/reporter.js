
module.exports = {
  reporter: function (issues) {
    issues.forEach(function(issue) {
      const error = issue.error;
      const result = {
        name: error.code,
        description: error.reason,
        location: {
          path: issue.file,
          line: error.line,
          column: error.character
        }
      };
      console.log(JSON.stringify(result));
    });
  }
};
