import math

import numpy as np


class Config:
    def __init__(self):
        self.learning_rate = 0.001


class Simulation:
    def __init__(self):
        self.env = InsulinControl()
        return

    def step(self, action):
        observation, reward, done = self.env.step(action)
        return observation, reward, done

    def legal_actions(self):
        legal_actions = self.env.legal_actions()
        return legal_actions

    def reset(self):
        return self.env.reset()

    def render(self):
        self.env.render()


class InsulinControl:
    def __init__(self):
        self.base_glucose = 99  # basal blood glucose level in plasma
        self.glucose = None  # blood glucose level in plasma
        self.insulin = None  # insulin concentration level in plasma
        self.base_insulin = 8  # basal insulin concentration level in plasma
        self.time = None  # the time interval from the glucose injection
        self.remote_insulin = None  # variable which is proportional to the insulin in the remote compartment
        self.P1 = 0  # the “glucose effectiveness” which represents the ability of blood glucose to enhance its own disposal at the basal insulin level
        self.P2 = 0.81 / 100  # decreasing level of insulin action with time
        self.P3 = 4.01 / 1000000
        self.gamma = 2.4 / 1000
        self.i_init = 192
        self.i_base = 8
        self.v_init = 0
        self.g_init = 337
        self.g_base = 99
        self.h = 93
        self.n = 0.23
        self.a = 2  # the time constant of the pump

    def step(self, action):
        observation = None
        reward = None
        done = None
        return observation, reward, done

    def legal_actions(self):
        legal_actions = None
        return legal_actions

    def formula(self):
        """
        All formulas are coded here. Uses later.
        x1 = self.g_init
        x2 = self.v_init
        x3 = self.i_init
        x4 = self.a  # w(t) = 1/2(-w(t) + u(t))

        t_time = None
        J_shape = (4, 4)
        J_x = np.zeros(J_shape)
        J_x[0, :] = np.array([-self.P1  -x2, -x1, 0, 0])
        J_x[1, :] = np.array([0, -self.P2, self.P3, 0])
        J_x[2, :] = np.array([self.gamma*t_time, 0, -self.n,1])
        J_x[3, :]= np.array([0, 0, 0, -1/self.a])

        J_u = np.array([[0],
                        [0],
                        [0],
                        [1/self.a]])
        x = None
        u = None

        #First fomula
        x_dot = J_x*x + J_u*u
        y = np.array([1,0,0,0])*x


        A = J_x
        B = np.array([[0],
                        [0],
                        [0],
                        [0.5]]) # B = J_u where u = 2
        C = np.array([1,0,0,0])

        a1 =None
        a2= None
        a3 = None
        a4 = None

        totient_A = pow(A,4) + a1*pow(A,3) + a2*pow(A,2) +a3*A,1+ a4*np.eye(4)
        matrix_CA = np.array([[C],
                      [C*A],
                      [C*(A**2)],
                      [C*(A**3)]])
        another_term = np.array([[0],
                      [0],
                      [0],
                      [1]])
        K_varepsilon = totient_A*np.linalg.inv(matrix_CA)*another_term

        K = np.array([0,0,0,1])*np.linalg.inv(np.array(B, A*B, A*A*B, (A**3)*B))*totient_A

        # x_tilde(t) is used to denote the observed state vector
        # x_tilde is the estimate state
        x_tilde = None

        # Second fomula
        x_tilde_dot = (A - K_varepsilon*C -B*K)*x_tilde + K_varepsilon*y
        """



