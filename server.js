const express = require('express');

const app = express();
const port = process.env.PORT || 8080;

// Serve static files
app.use(express.static('.'));

app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on port ${port}`);
});