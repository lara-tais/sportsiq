from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import SessionLocal
from app.models import Base, Quiz, Question

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# SQLAlchemy engine and session setup
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal.configure(bind=engine)

# Function to drop all tables
def recreate_db(engine):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Function to prepopulate the database
def prepopulate_db(db):
    # Recreate the database tables if necessary
    recreate_db(db.get_bind())
    # Create a Quiz
    quiz = Quiz(
        title="Example Quiz",
        sport="Football",
        level="Initial"
    )
    db.add(quiz)
    db.commit()

    # List of questions
    questions = [
        {
            "title": "What is the shape of a football?",
            "answers": {"a": "Square", "b": "Circle", "c": "Oval", "d": "Triangle"},
            "correct_answer": "c"
        },
        {
            "title": "How many points is a touchdown worth?",
            "answers": {"a": "1", "b": "2", "c": "3", "d": "6"},
            "correct_answer": "d"
        },
        {
            "title": "What is the name of the line that separates the offense and defense?",
            "answers": {"a": "Touchline", "b": "Baseline", "c": "Halfway line", "d": "Line of scrimmage"},
            "correct_answer": "d"
        },
        {
            "title": "What is the name of the person who throws the ball in football?",
            "answers": {"a": "Quarterback", "b": "Running back", "c": "Wide receiver", "d": "Linebacker"},
            "correct_answer": "a"
        },
        {
            "title": "How many players are on the field for one team at a time in football?",
            "answers": {"a": "5", "b": "7", "c": "9", "d": "11"},
            "correct_answer": "d"
        },
        {
            "title": "What is the name of the football league that professional teams play in?",
            "answers": {"a": "Major League Baseball (MLB)", "b": "National Football League (NFL)", "c": "National Basketball Association (NBA)", "d": "National Hockey League (NHL)"},
            "correct_answer": "b"
        },
        {
            "title": "What is the name of the big game that is played at the end of the NFL season?",
            "answers": {"a": "The World Series", "b": "The Super Bowl", "c": "The Stanley Cup Finals", "d": "The NBA Finals"},
            "correct_answer": "b"
        },
        {
            "title": "How many downs does an offense have to move the ball 10 yards?",
            "answers": {"a": "1", "b": "2", "c": "3", "d": "4"},
            "correct_answer": "d"
        },
        {
            "title": "What is the name of the player who kicks field goals and extra points?",
            "answers": {"a": "Kicker", "b": "Punter", "c": "Quarterback", "d": "Running back"},
            "correct_answer": "a"
        },
        {
            "title": "What is the name of the penalty where a player moves before the ball is snapped?",
            "answers": {"a": "Offside", "b": "Holding", "c": "Pass interference", "d": "False start"},
            "correct_answer": "d"
        },
        {
            "title": "What is the objective of football?",
            "answers": {"a": "Offside", "b": "Holding", "c": "Pass interference", "d": "False start"},
            "correct_answer": "d"
        },
        {
            "title": "What is the main responsibility of a cornerback in a Cover 2 defense?",
            "answers": {"a": "Defend against the deep pass", "b": "Defend against the short pass", "c": "Defend against the run", "d": "Blitz the quarterback"},
            "correct_answer": "b"
        },
        {
            "title": "What is the term used to describe when a cornerback lines up directly across from the wide receiver, with no help from a safety?",
            "answers": {"a": "Man-to-man coverage", "b": "Zone coverage", "c": "Press coverage", "d": "Cover 2"},
            "correct_answer": "a"
        },
        {
            "title": "What is the term used to describe when a cornerback drops back and covers a specific zone on the field, rather than following a specific receiver?",
            "answers": {"a": "Man-to-man coverage", "b": "Zone coverage", "c": "Press coverage", "d": "Cover 2"},
            "correct_answer": "b"
        },
        {
            "title": "When defending against a receiver running a 'slant' route, what is the best technique for a cornerback to use?",
            "answers": {"a": "Play inside leverage and undercut the route", "b": "Play outside leverage and force the receiver inside", "c": "Jam the receiver at the line of scrimmage", "d": "Play off-coverage and react to the route"},
            "correct_answer": "a"
        },
        {
            "title": "When defending against a 'double move' route, what is the best technique for a cornerback to use?",
            "answers": {"a": "Stay disciplined and avoid biting on the initial move", "b": "Jump the first move and try to intercept the pass", "c": "Play off-coverage and react to the route", "d": "Blitz the quarterback"},
            "correct_answer": "a"
        },
        {
            "title": "What is the primary responsibility of a cornerback in a cover 2 defense?",
            "answers": {"a": "Man-to-man coverage of a specific receiver", "b": "Playing the deep half of the field", "c": "Blitzing the quarterback", "d": "Defending the flat"},
            "correct_answer": "d"
        },
        {
            "title": "What is the purpose of press coverage?",
            "answers": {"a": "To disrupt the timing of the opposing quarterback's passing game", "b": "To protect against the deep pass", "c": "To force the opposing offense to run the ball", "d": "To allow the cornerback to get a better view of the play"},
            "correct_answer": "a"
        },
        {
            "title": "When should a cornerback look back to find the ball on a deep pass?",
            "answers": {"a": "As soon as the receiver starts to slow down", "b": "As soon as the receiver turns his head to locate the ball", "c": "As soon as the ball is released by the quarterback", "d": "As soon as the ball is within five yards of the receiver"},
            "correct_answer": "b"
        },
        {
            "title": "What is the purpose of a double move by a receiver?",
            "answers": {"a": "To fake out the cornerback and create separation for a deep pass", "b": "To draw the cornerback closer to the line of scrimmage", "c": "To give the quarterback more time to throw the ball", "d": "To allow the receiver to make a catch in traffic"},
            "correct_answer": "a"
        },
        {
            "title": "When should a cornerback attempt to jump a route?",
            "answers": {"a": "When he is confident he knows the play being run", "b": "When he is in man-to-man coverage", "c": "When the opposing quarterback has a reputation for throwing interceptions", "d": "When he has safety help over the top"},
            "correct_answer": "a"
        },
        {
            "title": "What is the primary responsibility of a cornerback in man-to-man coverage?",
            "answers": {"a": "Blitzing the quarterback", "b": "Covering the deep half of the field", "c": "Covering a specific receiver", "d": "Playing zone coverage"},
            "correct_answer": "c"
        },
        {
            "title": "What is a 'jam' technique in press coverage?",
            "answers": {"a": "Grabbing the receiver's jersey to slow them down", "b": "Using physical contact to disrupt the receiver's route", "c": "Dropping back into zone coverage", "d": "None of the above"},
            "correct_answer": "b"
        },
        {
            "title": "What is the goal of a cornerback in zone coverage?",
            "answers": {"a": "To prevent any pass completions in their area", "b": "To intercept every pass thrown in their area", "c": "To keep the play in front of them and make a tackle", "d": "To bait the quarterback into throwing a pass they can intercept"},
            "correct_answer": "c"
        },
        {
            "title": "What is a 'double move' route?",
            "answers": {"a": "A route where the receiver fakes a different route before breaking to the actual route", "b": "A route where two receivers run in parallel to each other", "c": "A route where the receiver runs deep and then comes back towards the line of scrimmage", "d": "A route where the receiver runs a quick slant before breaking to the outside"},
            "correct_answer": "a"
        },
        {
            "title": "What is a 'pick' play?",
            "answers": {"a": "A play where the quarterback fakes a handoff before passing to a receiver", "b": "A play where the offensive line intentionally holds the defensive line", "c": "A play where a receiver runs a route with the intention of blocking the defender covering another receiver", "d": "A play where the quarterback intentionally throws an interception"},
            "correct_answer": "c"
        },
        {
            "title": "What is the primary responsibility of a defensive end?",
            "answers": {"a": "Covering receivers", "b": "Stopping the run", "c": "Kicking field goals", "d": "Playing quarterback"},
            "correct_answer": "b"
        },
        {
            "title": "Which of the following is a common technique used by defensive ends to get past an offensive lineman?",
            "answers": {"a": "Spin move", "b": "Moonwalk", "c": "Cartwheel", "d": "Jumping jacks"},
            "correct_answer": "a"
        },
        {
            "title": "What is the term for the position of the defensive end on the line of scrimmage?",
            "answers": {"a": "Nose tackle", "b": "Slot receiver", "c": "Tight end", "d": "Defensive end"},
            "correct_answer": "d"
        },
        {
            "title": "Which of the following is a key trait for a successful defensive end?",
            "answers": {"a": "Speed", "b": "Strength", "c": "Agility", "d": "All of the above"},
            "correct_answer": "d"
        },
        {
            "title": "What is the term for when a defensive end tackles the quarterback behind the line of scrimmage?",
            "answers": {"a": "Sack", "b": "Touchdown", "c": "Fumble", "d": "Interception"},
            "correct_answer": "a"
        },
        {
            "title": "What is the primary goal of a defensive end in pass defense?",
            "answers": {"a": "Intercept the ball", "b": "Tackle the receiver", "c": "Disrupt the quarterback", "d": "None of the above"},
            "correct_answer": "c"
        },
        {
            "title": "What is the term for the area of the field where a defensive end lines up?",
            "answers": {"a": "End zone", "b": "Red zone", "c": "Line of scrimmage", "d": "Secondary"},
            "correct_answer": "c"
        },
        {
            "title": "Which of the following is a common responsibility for a defensive end in a 4-3 defense?",
            "answers": {"a": "Playing man-to-man coverage", "b": "Covering the slot receiver", "c": "Rushing the quarterback", "d": "None of the above"},
            "correct_answer": "c"
        },
        {
            "title": "What is the term for the defensive strategy where the defensive end lines up directly across from the offensive tackle?",
            "answers": {"a": "Cover 2", "b": "Man coverage", "c": "Zone coverage", "d": "Bull rush"},
            "correct_answer": "d"
        },
        {
            "title": "Which of the following is a common drill used to improve a defensive end's technique?",
            "answers": {"a": "Hitting a tackling dummy", "b": "Running sprints", "c": "Throwing a football", "d": "Shooting a basketball"},
            "correct_answer": "a"
        }
    ]

    # Add questions to the quiz
    for q in questions:
        question = Question(
            title=q["title"],
            answers=q["answers"],
            correct_answer=q["correct_answer"],
            quiz_id=quiz.id
        )
        db.add(question)

    db.commit()

# Run the script
if __name__ == "__main__":
    db = SessionLocal()
    try:
        prepopulate_db(db)
        print("Database prepopulated successfully!")
    finally:
        db.close()
