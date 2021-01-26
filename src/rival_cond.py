class RivalCond:
    upper_rate_limit = 100
    lower_rate_limit = 100
    upper_ranking_limit = 200
    lower_ranking_limit = 200
    required_pt_count = 5
    recent_contest_count = 10

    def to_dict(self):
        return {
            "upper_rate_limit": self.upper_rate_limit,
            "lower_rate_limit": self.lower_rate_limit,
            "upper_ranking_limit": self.upper_ranking_limit,
            "lower_ranking_limit": self.lower_ranking_limit,
            "required_pt_count": self.required_pt_count,
            "recent_contest_count": self.recent_contest_count
        }

    @staticmethod
    def from_dict( rival_cond_dict):
        rival_cond = RivalCond()
        rival_cond.upper_rate_limit = rival_cond_dict["upper_rate_limit"]
        rival_cond.lower_rate_limit = rival_cond_dict["lower_rate_limit"]
        rival_cond.upper_ranking_limit = rival_cond_dict["upper_ranking_limit"]
        rival_cond.lower_ranking_limit = rival_cond_dict["lower_ranking_limit"]
        rival_cond.required_pt_count = rival_cond_dict["required_pt_count"]
        rival_cond.recent_contest_count = rival_cond_dict["recent_contest_count"]
        return rival_cond
