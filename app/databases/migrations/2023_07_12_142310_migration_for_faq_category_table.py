"""MigrationForFaqCategoryTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForFaqCategoryTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("faqs_categories") as table:
            table.increments("id")
            table.jsonb("category")

            table.timestamps()
            table.timestamp("deleted_at").nullable()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("faqs_categories")
