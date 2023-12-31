"""MigrationForFaqTable Migration."""
from masoniteorm.migrations import Migration


class MigrationForFaqTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("faqs") as table:
            table.increments("id")
            table.integer("category_id").unsigned()
            table.foreign("category_id").references("id").on("faqs_categories")
            table.jsonb("faq")
            table.integer("visits").default(0)

            table.soft_deletes()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("faqs")
