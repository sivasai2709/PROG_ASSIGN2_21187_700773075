from ariadne import QueryType, MutationType, make_executable_schema

type_defs = """
type Query {
    runNLQuery(input: String!): String
    getAll(label: String!): String
}

type Mutation {
    create(label: String!, props: String!): String
    update(label: String!, name: String!, props: String!): String
    delete(label: String!, name: String!): String
}
"""

query = QueryType()
mutation = MutationType()