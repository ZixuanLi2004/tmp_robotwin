from ._base_task import Base_Task
from .utils import *
import sapien


class _final_task1(Base_Task):

    def setup_demo(self, **kwags):
        super()._init_task_env_(table_height_bias=0.0,**kwags)

    def load_actors(self):
        zz = self.table_z_bias
        objects_name = ["125_four-pin-plug", "126_junction-box", "128_scram-button", "130_three-pin-plug"]
        objects_qpos = [[0.707, 0.0, 0.707, 0.0], [0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5], [0.707, 0.0, 0.707, 0.0]]
        objects_rotate_lim = [[0.7, 0.0, 0], [0.0, 0.5, 0], [0.0, 0.3, 0], [0.7, 0.0, 0]]  
        objects_z = [1.044, 1.017, 1.017, 1.044]
        self.contact_id =[ [[8, 9, 10, 11, 12, 13, 14, 15], [1], [1,2,3,4], [0,5,6,7,8,9,10,11]], [[8, 9, 10, 11, 12, 13, 14, 15], [0], [1,2,3,4], [0,5,6,7,8,9,10,11]] ]
        self.ids = np.random.choice([0, 1, 2, 3], size=2, replace=False)
        # self.ids = [0, 0]  # 0: four-pin-plug, 1: junction-box, 2: scram-button, 3: three-pin-plug
        left_id, right_id = self.ids[0], self.ids[1]
        rand_pos = rand_pose(
            xlim=[0.0, 0.0],
            ylim=[-0.055, -0.055],
            zlim=[1.005+zz],
            qpos=[0.707, 0.707, 0.0, 0.0],
            rotate_rand=False,
        )
        self.box1= create_actor(
            scene=self,
            modelname="122_plastic-basket",
            model_id=7,
            pose = rand_pos,
            convex=True,
            is_static=True,
        )

        rand_pos = rand_pose(
            xlim=[0.47, 0.47],
            ylim=[-0.055, -0.055],
            zlim=[1.005+zz],
            qpos=[0.707, 0.707, 0.0, 0.0],
            rotate_rand=False,
        )
        self.box2= create_actor(
            scene=self,
            modelname="122_plastic-basket",
            model_id=7,
            pose = rand_pos,
            convex=True,
            is_static=True,
        )

        rand_pos = rand_pose(
            xlim=[-0.47, -0.47],
            ylim=[-0.055, -0.055],
            zlim=[1.005+zz],
            qpos=[0.707, 0.707, 0.0, 0.0],
            rotate_rand=False,
        )
        self.box3= create_actor(
            scene=self,
            modelname="122_plastic-basket",
            model_id=7,
            pose = rand_pos,
            convex=True,
            is_static=True,
        )

        self.object1: list[Actor] = []
        self.object1_id = []
        self.xlim = [[0.37, 0.6], [0.37, 0.6], [0.37, 0.6], [0.37, 0.6]]
        self.ylim = [[-0.11, -0.03], [-0.11, -0.03], [-0.11, -0.03], [-0.11, -0.03]]
        for i in range(3):
            rand_pos = rand_pose(
                xlim=self.xlim[right_id],
                ylim=self.ylim[right_id],
                zlim=[objects_z[right_id]],
                qpos=objects_qpos[right_id],
                rotate_rand=True,
                rotate_lim=objects_rotate_lim[right_id],
            )
            num = 0
            pd = False
            while True:
                pd = True
                num += 1
                for j in range(len(self.object1)):
                    peer_pose = self.object1[j].get_pose()
                    if ((peer_pose.p[0] - rand_pos.p[0])**2 + (peer_pose.p[1] - rand_pos.p[1])**2) < 0.02:
                        pd = False
                        break
                if pd == True or num > 50 :
                    break
                rand_pos = rand_pose(
                    xlim=self.xlim[right_id],
                    ylim=self.ylim[right_id],
                    zlim=[objects_z[right_id]],
                    qpos=objects_qpos[right_id],
                    rotate_rand=True,
                    rotate_lim=objects_rotate_lim[right_id],
                )
                
            if pd == True:
                id_list = [0]
                self.object1_id.append(np.random.choice(id_list))
                object1_actor = create_actor(
                    scene=self,
                    pose=rand_pos,
                    modelname=objects_name[right_id],
                    convex=True,
                    model_id=self.object1_id[i],
                    is_static=True,
                )
                self.object1.append(object1_actor)

        for i in range(len(self.object1)):
            self.add_prohibit_area(self.object1[i], padding=0.03)
            # self.object1[i].set_mass(0.07)

        
        self.object2: list[Actor] = []
        self.object2_id = []

        self.xlim = [[-0.6, -0.37], [-0.6, -0.37], [-0.6, -0.37], [-0.6, -0.37]]
        self.ylim = [[-0.11, -0.03], [-0.11, -0.03], [-0.11, -0.03], [-0.11, -0.03]]
        for i in range(3):
            rand_pos = rand_pose(
                xlim=self.xlim[left_id],
                ylim=self.ylim[left_id],
                zlim=[objects_z[left_id]],
                qpos=objects_qpos[left_id],
                rotate_rand=True,
                rotate_lim=objects_rotate_lim[left_id],
            )
            num = 0
            pd = False
            while True:
                pd = True
                num += 1
                for j in range(len(self.object2)):
                    peer_pose = self.object2[j].get_pose()
                    if ((peer_pose.p[0] - rand_pos.p[0])**2 + (peer_pose.p[1] - rand_pos.p[1])**2) < 0.02:
                        pd = False
                        break
                if pd == True or num > 50 :
                    break
                rand_pos = rand_pose(
                    xlim=self.xlim[left_id],
                    ylim=self.ylim[left_id],
                    zlim=[objects_z[left_id]],
                    qpos=objects_qpos[left_id],
                    rotate_rand=True,
                    rotate_lim=objects_rotate_lim[left_id],
                )
                
            if pd == True:
                id_list = [0]
                self.object2_id.append(np.random.choice(id_list))
                object2_actor = create_actor(
                    scene=self,
                    pose=rand_pos,
                    modelname=objects_name[left_id],
                    convex=True,
                    model_id=self.object2_id[i],
                    is_static=True,
                )
                self.object2.append(object2_actor)

        for i in range(len(self.object2)):
            self.add_prohibit_area(self.object2[i], padding=0.03)
            # self.object2[i].set_mass(0.07)

        self.add_prohibit_area(self.box1, padding=0.10)
        self.add_prohibit_area(self.box2, padding=0.10)
        self.add_prohibit_area(self.box3, padding=0.10)

        self.xlim = [[-0.1, 0.1], [-0.1, 0.1], [-0.1, 0.1], [-0.1, 0.1]]
        self.ylim = [[-0.13, -0.08], [-0.11, -0.03], [-0.11, -0.03], [-0.13, -0.08]]
        self.aim: list[Actor] = []
        self.aim_id = []
        for i in range(2):
            res = left_id if i == 0 else right_id
            rand_pos = rand_pose(
                xlim=self.xlim[self.ids[i]],
                ylim=self.ylim[self.ids[i]],
                zlim=[objects_z[self.ids[i]] + 0.01],
                qpos=objects_qpos[res],
                rotate_rand=True,
                rotate_lim=objects_rotate_lim[res],
            )
            while abs(rand_pos.p[0]) < 0.045:
                rand_pos = rand_pose(
                    xlim=self.xlim[self.ids[i]],
                    ylim=self.ylim[self.ids[i]],
                    zlim=[objects_z[self.ids[i]] + 0.01],
                    qpos=objects_qpos[res],
                    rotate_rand=True,
                    rotate_lim=objects_rotate_lim[res],
                )
            pd = False
            while True:
                pd = True
                for j in range(len(self.aim)):
                    peer_pose = self.aim[j].get_pose()
                    if ((peer_pose.p[0] - rand_pos.p[0])**2 + (peer_pose.p[1] - rand_pos.p[1])**2) < 0.01:
                        pd = False
                        break
                if pd == True:
                    break
                rand_pos = rand_pose(
                    xlim=self.xlim[self.ids[i]],
                    ylim=self.ylim[self.ids[i]],
                    zlim=[objects_z[self.ids[i]] + 0.01],
                    qpos=objects_qpos[res],
                    rotate_rand=True,
                    rotate_lim=objects_rotate_lim[res],
                )
                while abs(rand_pos.p[0]) < 0.045:
                    rand_pos = rand_pose(
                        xlim=self.xlim[self.ids[i]],
                        ylim=self.ylim[self.ids[i]],
                        zlim=[objects_z[self.ids[i]] + 0.01],
                        qpos=objects_qpos[res],
                        rotate_rand=True,
                        rotate_lim=objects_rotate_lim[res],
                    )
            if pd == True:
                id_list = [0]
                self.aim_id.append(np.random.choice(id_list))
                aim_actor = create_actor(
                    scene=self,
                    pose=rand_pos,
                    modelname=objects_name[res],
                    convex=True,
                    model_id=self.aim_id[i],
                )
                aim_actor.set_mass(0.05)
                self.aim.append(aim_actor)

        for i in range(len(self.aim)):
            self.add_prohibit_area(self.aim[i], padding=0.03)
            # self.aim[i].set_mass(0.07)
        
        self.state = True


    def play_once(self):
        left_arm_tag = ArmTag("left")
        right_arm_tag = ArmTag("right")
        # self.move(
        #     self.close_gripper(left_arm_tag, pos=0.7),
        #     self.close_gripper(right_arm_tag, pos=0.7),
        # )
        self.pre_arm = None
        self.pre_arm = self.pick_place(0)
        self.pick_place(id = 1)
        self.delay(4)

        objects_name = ["125_four-pin-plug", "126_junction-box", "128_scram-button", "130_three-pin-plug"]
        self.info["info"] = {
            "{A}": f"{objects_name[self.ids[0]]}/base0",
            "{a}": "left",
            "{B}": f"{objects_name[self.ids[1]]}/base0",
            "{b}": "right",
        }
        return self.info
    
    def pick_place(self, id):
        zz = self.table_z_bias
        arm_tag = ArmTag("left" if self.aim[id].get_pose().p[0] < 0 else "right")
        grasp_dis = [0.02, 0.025, 0.02, 0.02]
        res = 0 if str(arm_tag) == "left" else 1
        if self.pre_arm == None or self.pre_arm == arm_tag:
            if self.ids[id] == 1:
                self.move(self.close_gripper(arm_tag, pos=0.7))
            self.move(self.grasp_actor(
                actor=self.aim[id],
                arm_tag=arm_tag,
                pre_grasp_dis=0.07,
                grasp_dis=grasp_dis[self.ids[id]],
                gripper_pos=0.0,
                contact_point_id=self.contact_id[res][self.ids[id]]
            ))
        else:
            if self.ids[id] == 1:
                self.move(self.close_gripper(arm_tag, pos=0.7))
            self.move(self.grasp_actor(
                actor=self.aim[id],
                arm_tag=arm_tag,
                pre_grasp_dis=0.07,
                grasp_dis=grasp_dis[self.ids[id]],
                gripper_pos=0.0,
                contact_point_id=self.contact_id[res][self.ids[id]]
                ),
                self.back_to_origin(self.pre_arm)
            )
        if id == 0:
            if self.ids[id] == 1:
                target_pose = self.box3.get_functional_point(1, "pose")
            else:
                target_pose = self.box3.get_functional_point(2, "pose")
            target_qpose = [[0.707, 0, 0.707, 0], [1,0,0,0], [1,0,0,0], [0.707, 0, 0.707, 0]]
            target_pose.q = target_qpose[self.ids[id]]
        else:
            if self.ids[id] == 1:
                target_pose = self.box2.get_functional_point(0, "pose")
            else:
                target_pose = self.box2.get_functional_point(2, "pose")
            target_qpose = [[0.707, 0, -0.707, 0], [1,0,0,0], [1,0,0,0], [0.707, 0, -0.707, 0]]
            target_pose.q = target_qpose[self.ids[id]]
    
        place_dis = [0.07, 0.04, 0.07, 0.07]
        lift_dis = [0.05, 0.08, 0.05, 0.05]
        if (str(arm_tag) == "left" and id == 0) or (str(arm_tag) == "right" and id == 1):
            if str(arm_tag) == "left":
                self.move(self.move_by_displacement(arm_tag, z=0.135+zz, x=-0.05))
            else:
                self.move(self.move_by_displacement(arm_tag, z=0.135+zz, x=0.05))
            if self.ids[id] == 0 or self.ids[id] == 3:
                place_gripper_pos = self.get_arm_pose(arm_tag)[:3]
                ee_quat = [0.605, -0.443, 0.387, 0.537]
                # pdb.set_trace()
                dis_x, dis_y = target_pose.p[0] - place_gripper_pos[0], target_pose.p[1] - place_gripper_pos[1]
                dis_z = 1.35 - place_gripper_pos[2] +zz
                self.move(self.move_by_displacement(arm_tag, x=dis_x, y=dis_y, z=dis_z, quat=ee_quat))
                self.move(self.move_by_displacement(arm_tag, z = -0.07))
                self.move(self.open_gripper(arm_tag, pos=0.85))
            else:
                self.move(self.place_actor(
                    self.aim[id],
                    arm_tag=arm_tag,
                    target_pose=target_pose,
                    pre_dis=0.133,
                    dis=place_dis[self.ids[id]],
                    constrain = "free"
                ))
            self.move(self.move_by_displacement(arm_tag, z=lift_dis[self.ids[id]]))
            return arm_tag
        else:
            if str(arm_tag) == "left":
                self.move(self.move_by_displacement(arm_tag, z=0.1+zz))
            else:
                self.move(self.move_by_displacement(arm_tag, z=0.1+zz))
            aim_pose = [0, -0.15, 1.155, 0, 0, 0, 0]
            place_arm = arm_tag.opposite
            aim_pose[0] -= 0.05 if str(arm_tag) == "left" else -0.05
            aim_pose[3:] = [1, 0, 0, 0]
            self.move(self.place_actor(
                self.aim[id],
                arm_tag=arm_tag,
                target_pose=aim_pose,
                pre_dis=0.0,
                dis=0.0,
                constrain = "free",
                is_open=False
            ))
            
            if self.ids[id] == 2:
                res = 0 if str(place_arm) == "left" else 6
                self.move(self.grasp_actor(
                    actor=self.aim[id],
                    arm_tag=place_arm,
                    pre_grasp_dis=0.15,
                    grasp_dis=0.06,
                    gripper_pos=0.0,
                    contact_point_id=[res]
                ))
                self.move(self.open_gripper(arm_tag, pos=0.8))
                self.move(self.move_by_displacement(arm_tag, z=0.05))
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, x=-0.2))
                else:
                    self.move(self.move_by_displacement(place_arm, x=0.2))
                place_gripper_pos = self.get_arm_pose(place_arm)[:3]
                ee_quat = [0.605, -0.443, 0.387, 0.537]
                dis_x, dis_y = target_pose.p[0] - place_gripper_pos[0], target_pose.p[1] - place_gripper_pos[1]
                dis_z = 1.35 - place_gripper_pos[2] + zz
                self.move(
                    self.move_by_displacement(place_arm, x=dis_x, y=dis_y, z=dis_z, quat=ee_quat),
                    self.back_to_origin(arm_tag)
                )
                self.move(self.move_by_displacement(place_arm, z = -0.16 + zz))
                self.move(self.open_gripper(place_arm, pos=1))
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, z=0.2 + zz, x=0.25,y=-0.1))
                else:
                    self.move(self.move_by_displacement(place_arm, z=0.2 + zz, x=-0.25,y=-0.1))
                return place_arm
            elif self.ids[id] == 1:
                res = 3 if str(place_arm) == "left" else 2
                self.move(self.close_gripper(place_arm, pos=0.8))
                self.move(self.grasp_actor(
                    actor=self.aim[id],
                    arm_tag=place_arm,
                    pre_grasp_dis=0.1,
                    grasp_dis=0.02,
                    gripper_pos=0.33,
                    contact_point_id=res
                ))
                self.move(self.open_gripper(arm_tag, pos=0.69))
                self.move(self.move_by_displacement(arm_tag, z=0.05))
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, x=-0.2,z=0.1))
                else:
                    self.move(self.move_by_displacement(place_arm, x=0.2,z=0.1))
                target_pose.q = [0.707, 0, 0.707, 0] if str(place_arm) == "left" else [0.707, 0, -0.707, 0]
                self.move(self.place_actor(
                    self.aim[id],
                    arm_tag=place_arm,
                    target_pose=target_pose,
                    pre_dis=0.175,
                    dis=0.07,
                    constrain = "free"
                    ),
                    self.back_to_origin(arm_tag)
                )
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, z=0.2, x=0.1))
                else:
                    self.move(self.move_by_displacement(place_arm, z=0.2, x=-0.1))
                return place_arm
            elif self.ids[id] == 0 or  self.ids[id] == 3:
                res = [16, 17 , 18, 19, 20, 21, 22, 23] if self.ids[id] == 0 else [12, 13, 14, 15, 16, 17, 18, 19]
                self.move(self.grasp_actor(
                    actor=self.aim[id],
                    arm_tag=place_arm,
                    pre_grasp_dis=0.15,
                    grasp_dis=0.055,
                    gripper_pos=0.01,
                    contact_point_id=res
                ))
                self.move(self.open_gripper(arm_tag, pos=0.8))
                self.move(self.move_by_displacement(arm_tag, z=0.03))
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, x=-0.2, z=0.1))
                else:
                    self.move(self.move_by_displacement(place_arm, x=0.2, z=0.1))
                # target_pose.q = [0.707, 0, 0.707, 0] if str(place_arm) == "left" else [0.707, 0, -0.707, 0]
                place_gripper_pos = self.get_arm_pose(place_arm)[:3]
                ee_quat = [0.605, -0.443, 0.387, 0.537]
                # pdb.set_trace()
                dis_x, dis_y = target_pose.p[0] - place_gripper_pos[0], target_pose.p[1] - place_gripper_pos[1]
                dis_z = 1.3 - place_gripper_pos[2] + zz
                # self.move(self.place_actor(
                #     self.aim[id],
                #     arm_tag=place_arm,
                #     target_pose=target_pose,
                #     pre_dis=0.165,
                #     dis=0.06,
                #     constrain = "free"
                #     ),
                #     self.back_to_origin(arm_tag)
                # )
                self.move(
                    self.move_by_displacement(place_arm, x=dis_x, y=dis_y, z=dis_z, quat=ee_quat),
                    self.back_to_origin(arm_tag)
                )
                self.move(self.move_by_displacement(place_arm, z = -0.07 + zz))
                self.move(self.open_gripper(place_arm, pos=0.8))
                if str(place_arm) == "left":
                    self.move(self.move_by_displacement(place_arm, z=0.2 + zz, x=0.25,y=-0.1))
                else:
                    self.move(self.move_by_displacement(place_arm, z=0.2 + zz, x=-0.25,y=-0.1))
                return place_arm


    def check_success(self):
        # return True
        target_pose0 = self.box3.get_pose() 
        target_pose1 = self.box2.get_pose()
        return (np.sqrt(np.sum((self.aim[0].get_pose().p[:2] - target_pose0.p[:2]) ** 2)) < 0.2) and \
                (np.sqrt(np.sum((self.aim[1].get_pose().p[:2] - target_pose1.p[:2]) ** 2)) < 0.2) and \
                self.aim[0].get_pose().p[2] > 1.0 and self.aim[1].get_pose().p[2] > 1.0
