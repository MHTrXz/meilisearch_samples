const express = require('express');
const app = express();
const cors = require('cors');
const { MeiliSearch } = require('meilisearch');
const movies = require('./movies.json'); // Ensure the path is correct

const client = new MeiliSearch({
    host: 'http://localhost:7700',
    apiKey: '9fcd362f8393402884e17349b5d2426888c479cd'
})

client.index('movies').addDocuments(movies)
    .then((response) => {
        console.log('Documents added to Meilisearch index:', response);
    })
    .catch((error) => {
        console.error('Error adding documents to Meilisearch:', error);
    });

// Middleware to parse JSON bodies
app.use(express.json());
app.use(cors());

// Endpoint to search for movies
app.get('/search', async (req, res) => {
    const query = req.query.q;

    if (!query) {
        return res.status(400).json({ error: 'Query parameter "q" is required' });
    }

    try {
        const searchResults = await client.index('movies').search(query);
        res.json(searchResults.hits);
        console.log(searchResults.hits);
    } catch (err) {
        console.error('Search error:', err);
        res.status(500).json({ error: 'An error occurred while searching' });
    }
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
