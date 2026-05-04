import convert_tables
import convert_temp_tables
import convert_views
import convert_mviews
import convert_functions
import convert_procedures
import convert_triggers

if __name__ == "__main__":
    convert_tables.run()
    convert_temp_tables.run()
    convert_views.run()
    convert_mviews.run()
    convert_functions.run()
    convert_procedures.run()
    convert_triggers.run()
    print("✅ Full Sybase → Oracle conversion completed")
