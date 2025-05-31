from utils.creator.src.databases.query import Query
class Relation:  

    # One-to-One relationship
    def one_to_one(self, table1, table2, fk_column, pk_column='id'):
        """
        Fetches a one-to-one relationship. Assumes table2 has a foreign key referencing table1.
        """
        self.sql = f"""
        SELECT t1.*, t2.*
        FROM {table1} AS t1
        JOIN {table2} AS t2
        ON t1.{pk_column} = t2.{fk_column}
        """
        return self

    # One-to-Many relationship
    def one_to_many(self, table1, table2, fk_column, pk_column='id'):
        """
        Fetches a one-to-many relationship. Assumes table2 has a foreign key referencing table1.
        """
        self.sql = f"""
        SELECT t1.*, t2.*
        FROM {table1} AS t1
        LEFT JOIN {table2} AS t2
        ON t1.{pk_column} = t2.{fk_column}
        """
        return self

    # Many-to-Many relationship
    def many_to_many(self, table1, table2, pivot_table, fk1, fk2, pk1='id', pk2='id'):
        """
        Fetches a many-to-many relationship. Assumes there is a pivot table linking table1 and table2.
        """
        self.sql = f"""
        SELECT t1.*, t2.*
        FROM {table1} AS t1
        JOIN {pivot_table} AS p ON t1.{pk1} = p.{fk1}
        JOIN {table2} AS t2 ON t2.{pk2} = p.{fk2}
        """
        return self
