from flask import flash

class Survey:
    

    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid

    
