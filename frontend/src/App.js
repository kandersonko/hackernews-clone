import React from 'react';
import gql from 'graphql-tag';
import { Query } from 'react-apollo';

const GET_LINKS = gql`
  {
    links {
      id
      url
      description
      postedBy {
        id
        username
      }
    }
  }
`;

const Links = ({ onLinkSelected }) => (
  <Query query={GET_LINKS}>
    {({ loading, error, data }) => {
      if (loading) return 'Loading...';
      if (error) return `Error! ${error.message}`;
      console.log('data: ', data);
      
      return (
        <div>
          {data.links.map(dog => (
            <li key={dog.id}>
              {dog.url}
            </li>
          ))}
        </div>
      );
    }}
  </Query>
);

const App = () => (
  <div>
    Popular links:
    <Links />
  </div>
);

export default App;